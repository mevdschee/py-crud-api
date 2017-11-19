from wsgiref.simple_server import make_server

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return b"Hello World!"

make_server('127.0.0.1', 8080, app).serve_forever()
