import jinja_env
import logging
import webapp2
from google.appengine.api import users



class EddiePartHandler(webapp2.RequestHandler):
	def get(self):
		logging.info("EddiePartHandler")
		current_user = users.get_current_user()
		if current_user== None:
			self.redirect("/")
		else:
			html_params = {
	         'email': current_user.email()
			}

			template = jinja_env.env.get_template('templates/profile.html')
			self.response.out.write(template.render(html_params))

		