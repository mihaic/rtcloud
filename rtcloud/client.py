import os
import pika
import requests
from binaryornot.check import is_binary


def get_paths(input_dir='.'):
    # Python checks path based on current working directory
    cwd = os.getcwd()
    os.chdir(input_dir)
    paths = [os.path.abspath(path) for path in os.listdir()]
    paths = filter(os.path.isfile, paths)
    os.chdir(cwd)

    return paths


def open_path(path):
    return open(path, 'r%s' % ('b' if is_binary(path) else ''))


class Client():
    def __init__(self, server_address=None, conf=None):
        assert server_address is not None, 'server_address required'
        assert conf is not None, 'conf required'

        self.server_address = server_address
        self.conf = conf
        self.connected = False
        self.name = 'rtcloud'
        self.conf['name'] = self.name

    def start(self):
        req = requests.post(os.path.join(self.server_address, 'start'),
                            data=self.conf)

        if req.status_code == 200:
            self.connected = True

    def queue(self, input_dir='.', tr=2000, loop=True, watch=False):
        assert self.connected, 'Not connected to server!'

        rmq = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = rmq.channel()
        channel.queue_declare(queue=self.name)

        paths = get_paths(input_dir)
        for path in paths:
            print(path)
            channel.basic_publish(
                    exchange='',
                    routing_key=self.name,
                    body=open_path(path).read()
                    )

    def upload(self, input_dir='.', tr=2000, loop=True, watch=False):
        assert self.connected, 'Not connected to server!'

        paths = get_paths(input_dir)

        for path in paths:
            req = requests.post(os.path.join(self.server_address, 'upload'),
                                files={
                'file': open_path(path)
            })

            # TODO: Fail gracefully
            assert req.status_code == 202

    def watch(self, result_queue=None, callback=lambda *args: None):
        assert self.connected, 'Not connected to server!'
        assert result_queue is not None, 'result_queue required'
