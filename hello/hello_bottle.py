from bottle import route, run

@route('/')
def index():
    return b'Hello world!'

run(host='localhost', port=8080)
