
import jinja_env
import logging
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("MainHandler")
    	# logging.info(users.create_login_url())




    	# author = users.get_current_user()

    	


    	# current_user = users.get_current_user()

     #    user_comments_query = Comment.query(Comment.author == current_user.email())
     #    user_comments = user_comments_query.fetch()
     	html_params = {
            "title": "SAVE IT UP",
            "content": "Hello"
     #        "html_login_url": users.create_login_url("/")
     #        "html_current_user": current_user,
        }
        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))