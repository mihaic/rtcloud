import os
import requests
from binaryornot.check import is_binary


class Client():
    def __init__(self, server_address=None, conf=None):
        assert server_address is not None, 'server_address required'
        assert conf is not None, 'conf required'

        self.server_address = server_address
        self.conf = conf
        self.connected = False

    def start(self):
        req = requests.post(os.path.join(self.server_address, 'start'),
                            data=self.conf)

        if req.status_code == 200:
            self.connected = True

    def upload(self, input_dir='.', tr=2000, loop=True, watch=False):
        assert self.connected, 'Not connected to server!'

        # Python checks path based on current working directory
        cwd = os.getcwd()
        os.chdir(input_dir)
        paths = [os.path.abspath(path) for path in os.listdir()]
        paths = filter(os.path.isfile, paths)
        os.chdir(cwd)

        for path in paths:
            req = requests.post(os.path.join(self.server_address, 'upload'),
                                files={
                'file': open(path, 'r%s' % ('b' if is_binary(path) else ''))
            })

            # TODO: Fail gracefully
            assert req.status_code == 202

    def watch(self, result_queue=None, callback=lambda *args: None):
        assert self.connected, 'Not connected to server!'
        assert result_queue is not None, 'result_queue required'
