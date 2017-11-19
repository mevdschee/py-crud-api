import bjoern, os

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return b'Hello World!'

bjoern.listen(application, "localhost", 8080)
bjoern.run()
