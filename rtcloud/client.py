import os
import time
import pika
import requests
from binaryornot.check import is_binary
from pathos.helpers import mp


def get_paths(input_dir='.'):
    # Python checks path based on current working directory
    cwd = os.getcwd()
    os.chdir(input_dir)
    paths = [os.path.abspath(path) for path in os.listdir()]
    paths = list(filter(os.path.isfile, paths))
    os.chdir(cwd)

    return paths


def get_channel(address, queue):
    rmq = pika.BlockingConnection(pika.ConnectionParameters(address))
    channel = rmq.channel()
    channel.queue_declare(queue=queue)

    return channel


def open_path(path):
    return open(path, 'r%s' % ('b' if is_binary(path) else ''))


class Client():
    def __init__(self, server_ip=None, conf=None, http_endpoint='brainiak',
            server_port=21216, rmq_port=5672):
        assert server_ip is not None, 'server_address required'
        assert conf is not None, 'conf required'

        self.server_ip = server_ip
        self.server_port = server_port

        self.server_address = 'http://%s:%d' % \
                (self.server_ip, self.server_port)
        self.server_address = os.path.join(self.server_address, http_endpoint)

        self.rmq_port = rmq_port
        self.conf = conf
        self.connected = False
        self.name = 'rtcloud'
        self.queue_work_name = '%s_work' % self.name
        self.queue_result_name = '%s_result' % self.name

        self.conf['name'] = self.name
        self.conf['queue_work_name'] = self.queue_work_name
        self.conf['queue_result_name'] = self.queue_result_name

    def start(self):
        req = requests.post(os.path.join(self.server_address, 'start'),
                data=self.conf)

        if req.status_code == 200:
            self.connected = True

    def queue(self, input_dir='.', tr=2000, loop=True, watch=False):
        assert self.connected, 'Not connected to server!'

        def queue_helper(queue_work_name, input_dir, tr, loop):
            # NOTE: Each process needs its own set of file descriptors
            # TODO: parameterize address
            channel = get_channel('localhost', queue_work_name)
            paths = get_paths(input_dir)

            while True:
                for path in paths:
                    channel.basic_publish(
                            exchange='',
                            routing_key=queue_work_name,
                            body=open_path(path).read()
                            )
                    time.sleep(float(tr / 1000))
                if not loop:
                    break

        process = mp.Process(target=queue_helper, args=(
            self.queue_work_name,
            input_dir,
            tr,
            loop,
            ))

        process.start()

        return

    def upload(self, input_dir='.', tr=2000, loop=True, watch=False):
        assert self.connected, 'Not connected to server!'

        paths = get_paths(input_dir)

        for path in paths:
            req = requests.post(os.path.join(self.server_address, 'upload'),
                    files={'file': open_path(path)})

            # TODO: Fail gracefully
            assert req.status_code == 202

    def watch(self, callback=lambda *args: None):
        assert self.connected, 'Not connected to server!'
        print('Starting to watch!')

        def watch_helper(queue_result_name, callback):
            channel = get_channel('localhost', queue_result_name)

            def callback_rmq(channel, method, properties, body):
                callback(body)

            channel.basic_consume(
                    callback_rmq,
                    queue=queue_result_name,
                    no_ack=True)
            channel.start_consuming()

        process = mp.Process(target=watch_helper, args=(
            self.queue_result_name,
            callback,
            ))

        process.start()

        return

