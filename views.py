import cherrypy
from cherrypy import expose

import os
import urllib
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Index(object):
    @cherrypy.expose
    def index(self):
        template = JINJA_ENVIRONMENT.get_template('app/index.html')
        return template.render()
