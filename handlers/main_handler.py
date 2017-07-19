
import jinja_env
import logging
import webapp2
from google.appengine.api import users

from google.appengine.ext import ndb

class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info(users.get_current_user())
        logging.info(users.create_login_url())
       
   


        current_user = users.get_current_user()
        




        html_params = {
            "title": "SAVE IT UP",
            "content": "Hello",
            "html_login_url": users.create_login_url("/second"),
            "html_current_user": current_user,
            
        }
        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))


 
    def post(self):
            author = user.get_current_user()
            if author != None:

                 self.redirect("/")


 
class FriendList(webapp2.RequestHandler):
    def get(self):
    	logging.info(user.get_search_friend())



    	html_friend = user.get_search_friend()

    	html_friends = {
    		"html_friendlist": html_friend,


    	}



 	template = jinja_env.env.get_template('templates/friend.html')
        self.response.out.write(template.render(html_friends))


        def post(self):
        	html_friend = user.get_search_friend()
        	if html_friend != None:
        			self.redirect('/second')








    



