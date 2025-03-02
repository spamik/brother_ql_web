#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('/opt/brother_ql_web')
from app import create_app

app = create_app()
application = app

if __name__ == "__main__":
    app.run(host = app.config['SERVER_HOST'], port = app.config['SERVER_PORT'])
