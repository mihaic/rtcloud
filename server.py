import os
import sys
import json
import argparse

from rtcloud.utils import Logger

from flask import Flask, request, redirect, url_for, flash, session, send_from_directory
from werkzeug.utils import secure_filename
from flask_session import Session

import rtcloud.experiments

class BrainiakCloud:
    def __init__(self, opts):
        self.app = Flask(__name__)
        self.BASE_URL = '/' + opts.get('BASE_URL')

        # Debug utilities
        self.logger = Logger()

        # Configure
        self.app.config['UPLOAD_FOLDER'] = opts.get('UPLOAD_FOLDER')
        self.ALLOWED_EXTENSIONS = set(opts.get('ALLOWED_EXTENSIONS'))

        # Initialize secrets
        # TODO: Add Config to handle secret data
        self.app.secret_key = 'super secret key'

        # Initialize session
        self.session = Session()
        self.app.config['SESSION_TYPE'] = 'filesystem'
        self.session.init_app(self.app)

        # Initialize routes
        self.app.add_url_rule(self.BASE_URL, '/', self.index, methods=['GET'])
        self.app.add_url_rule(self.BASE_URL, 'upload', self.upload, methods=['POST'])

        # Initialize experiment
        self.experimentClass = getattr(experiments, opts.get('experimentClass'))
        self.experiment = self.experimentClass(opts)

        # Ready to roll
        self.app.debug = opts.get('DEBUG')
        self.app.run(host='0.0.0.0')

    def allowed_file(self, filename):
        # TODO: This is a crappy way to check extensions
        return '.' in filename and \
                filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    def index(self):
        return 'Hello, world!'

    # TODO: Have any semblance at all of error handling
    def upload(self):
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(self.app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            self.experiment.process(filepath)

            return 'Success!'
        return 'FAIL!'

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('conf', help='path to configuration (*.json)')
    args = arg_parser.parse_args()

    opts = {}
    with open(args.conf) as json_data:
        # TODO: Error handling
        # TODO: Check schema and print usage if wrong
        opts = json.load(json_data)

    server = BrainiakCloud(opts)
