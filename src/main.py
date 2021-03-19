import re
from flask import request
from flask import Flask
from flask import logging
from flask import jsonify
import subprocess
import time
import os
import sys

# configure application
app = Flask(__name__)
port = 8080


def get_rev_hash():
    return subprocess.check_output(['git', 'rev-parse', 'HEAD'])


@app.after_request
def log_request_status(response):
    t = time.localtime()
    status_text = response.status
    status = response.status_code
    print("[{}] {} {}".format(time.strftime(
        "%H:%M:%S", t), request.full_path, status))

    return response


def split_name_by_uppercase(name):
    split_name = re.sub(r"([A-Z])",  r" \1", name).strip()
    return split_name


@app.route('/helloworld')
def helloworld():
    username = request.args.get('name')
    if username:
        print(username)
        username = split_name_by_uppercase(username)
    else:
        username = 'Stranger'
    return 'Hello ' + username


@app.route('/versionz')
def versionz():
    return jsonify(
        project_name="Endocode Challenge",
        project_hash=get_rev_hash()
    )


if __name__ == "__main__":
    # check if a port was set by the command line
    if len(sys.argv) > 1:
        port = sys.argv[1]
    # if an env variable exists then override the port configuration
    if 'ENDO_PORT' in os.environ:
        port = os.environ['ENDO_PORT']

    # disable logging
    log = logging.logging.getLogger('werkzeug')
    log.setLevel(logging.logging.FATAL)

    # run application
    app.run(host='0.0.0.0', port=port)
