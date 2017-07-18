#Makes a new page for tracking items
import jinja_env
import logging
import webapp2
class TrackItemHandler(webapp2.RequestHandler):
	def get(self):
		logging.info("TrackItemHandler")
		html_params = {
			"title": "Tracked Item List",
			"content": "Selected Items Listed Below:"
		}
		template = jinja_env.env.get_template('templates/Track.html')
		self.response.out.write(template.render(html_params))

#Get information for comments and post of images
	def post(self):
		logging.info("USER SAID POST")
		r_user = self.request.get("usrform")
		r_form = self.request.get("fileToUpload")
		r_comit = self.request.get("comment")

		TrackItem = Save_Model. SaveModel(
			username= r_user,)
		self.redirect("/progress")

 


