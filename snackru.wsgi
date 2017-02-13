#!/usr/bin/python

import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/snackru/")

from xd import app as application
application.secret_key = "snackru"
