
import jinja_env
import logging
import webapp2

from models import book

class SecondHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("SecondHandler")
    	books = book.Book.query().fetch()
    	# do stuff with books...
        html_params = {
            "title": "Second Title",
            "content": "Goodbye"
        }
        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))