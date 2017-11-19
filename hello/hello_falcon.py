import falcon

class HelloResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = '"Hello World!"'

app = falcon.API()

app.add_route('/', HelloResource())
