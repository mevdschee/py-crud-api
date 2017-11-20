import bjoern, os

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return b'Hello World!'

if __name__ == "__main__":
    bjoern.listen(application, "localhost", 8080)
    bjoern.run()
