
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


# class Comment(ndb.Model):
#           author = ndb.StringProperty()


    def post(self):
            author = user.get_current_user()
            if author != None:

                 self.redirect("/")



# class FriendList(webapp2.RequestHandler):
    # def get(self):
        







    



