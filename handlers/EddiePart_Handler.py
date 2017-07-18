import jinja_env
import logging
import webapp2


class EddiePartHandler(webapp2.RequestHandler):
	def get(self):
		logging.info("EddiePartHandler")

		html_params = {
		}

		template = jinja_env.env.get_template('templates/profile.html')
		self.response.out.write(template.render(html_params))

		