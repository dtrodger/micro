#! /usr/local/env python

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from project import create_app

if __name__ == '__main__':
    app = create_app(config_name='deploy')
    app.run(
        host='0.0.0.0',
        port=80,
        debug=False
    )
