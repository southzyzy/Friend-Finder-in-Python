"""
run:
Author: @ Tan Zhao Yea

This part holds all the codes to make the Friend Finder GUI workable.

The GUI runs on a webserver, WSGIserver.
    1. Start the application's GUI on localhost.
    2. Simply run python run.py and go to browswer and enter localhost:1000 to access the Friend Finder GUI

Monkey:
The primary purpose of this module is to carefully patch, in place, portions of the standard library with gevent-friendly functions that behave in the same way as the original

Read More:
WSGIserver: https://pypi.org/project/WSGIserver/
gevent.Monkey:
"""

from gevent import monkey
monkey.patch_all() # Patching should be done as early as possible in the lifecycle of the program
from app import app
from gevent.pywsgi import WSGIServer
import warnings

try:
    warnings.filterwarnings('ignore')
    print("-> Starting GUI on addr: localhost:1000")

    http_server = WSGIServer(('0.0.0.0', 1000), app) # intialise the WSGI Server
    http_server.serve_forever() # serve the server

except KeyboardInterrupt:
    pass

except Exception as e:
    print('Exception: {}'.format(e))
