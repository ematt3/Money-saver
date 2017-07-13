import os
import webapp2

from handlers import jinja_env
from handlers import main_handler
from handlers import second_handler

jinja_env.init(os.path.dirname(__file__))

app = webapp2.WSGIApplication([
    ('/', main_handler.MainHandler),
    ('/second', second_handler.SecondHandler),
], debug=True)
