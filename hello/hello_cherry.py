"""Hello world example in CherryPy."""
import cherrypy

class HelloWorld(object):
    """Hello world class."""
    def index(self):
        """Returns hello world string."""
        return "Hello World!"
    index.exposed = True

cherrypy.quickstart(HelloWorld())
