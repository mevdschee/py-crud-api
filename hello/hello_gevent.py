#!/usr/bin/python
"""WSGI server"""
from gevent.pywsgi import WSGIServer


def application(env, start_response):
    """HTTP handler"""
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return b"Hello world!"

if __name__ == '__main__':
    WSGIServer(('', 8080), application).serve_forever()
