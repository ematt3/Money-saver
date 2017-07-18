
import jinja_env
import logging
import webapp2


from models import money_model
class SecondHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("SecondHandler")
        money = money_model.moneyModel.query().fetch()

        html_params = {
            "title": "Getting Started",
        }
        template = jinja_env.env.get_template('templates/gettingstarted.html')
        self.response.out.write(template.render(html_params))

    def post(self):

        logging.info("There was a post")
        r_user = self.request.get("form_user")

        new_user = money_model.moneyModel(
            user_responses = r_user,
            )
        new_user.put()
        self.redirect("/profile")
