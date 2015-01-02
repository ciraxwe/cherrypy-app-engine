import cherrypy
import wsgiref.handlers
import views

root = views.Index()

# Start CherryPy app in wsgi mode
app = cherrypy.tree.mount(root, "/")
wsgiref.handlers.CGIHandler().run(app)
