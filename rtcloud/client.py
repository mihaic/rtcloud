class Client():
    def __init__(self, server_address=None, conf=None):
        assert server_address is not None, "server_address required"
        assert conf is not None, "conf required"

        self.server_address = server_address
        self.conf = conf

    def upload(self, input_dir='.', tr=2000, loop=True):
        assert self.server_address is not None, "init not called"

    def watch(self, result_queue=None, callback=lambda *args: None):
        assert self.server_address is not None, "init not called"
        assert result_queue is not None, "result_queue required"
