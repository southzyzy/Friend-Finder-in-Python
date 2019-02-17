"""
run:
This part holds all the codes to make the Friend Finder GUI workable.

The GUI runs on a webserver, WSGIserver.
    1. Start the application's GUI on localhost. 

Read More:
WSGIserver: https://pypi.org/project/WSGIserver/
"""

from gevent import monkey
monkey.patch_all()
from app import app
from gevent.pywsgi import WSGIServer
import warnings

try:
    warnings.filterwarnings('ignore')
    print("-> Starting GUI on addr: localhost:1000")

    http_server = WSGIServer(('0.0.0.0', 1000), app)
    http_server.serve_forever()

except KeyboardInterrupt:
    pass

except Exception as e:
    print('Exception: {}'.format(e))
