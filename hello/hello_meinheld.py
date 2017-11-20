from meinheld import server
 
def hello_world(environ, start_response):
    start_response('200 OK', [('Content-type','text/plain')])
    return 'Hello world!'
 
server.set_access_logger(None)

if __name__ == "__main__":
    server.listen(("0.0.0.0", 8000))
    server.run(hello_world)
