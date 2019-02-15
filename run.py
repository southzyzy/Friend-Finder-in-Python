from gevent import monkey

monkey.patch_all()
from app import app
from gevent.pywsgi import WSGIServer

try:
    print("-> Starting GUI on addr: localhost:1000")
    http_server = WSGIServer(('0.0.0.0', 1000), app)
    http_server.serve_forever()

except KeyboardInterrupt:
    pass

except Exception as e:
    print('Exception: {}'.format(e))
