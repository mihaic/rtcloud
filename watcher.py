import argparse
import requests

import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input-directory',
                    help='Input directory to watch', default='.')
parser.add_argument('-o', '--output-url', help='Output URL to upload to')
args = parser.parse_args()


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)
        req = requests.post(args.output_url, files={
            'file': open(event.src_path, 'rb')
        })

        print(req.text)


observer = Observer()
observer.schedule(Handler(), args.input_directory, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
