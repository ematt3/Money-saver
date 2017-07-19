
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
        r_price = self.request.get("form_price")
        r_time = self.request.get("form_time")
        r_monthlyWage = self.request.get("form_monthly_wage")
        r_currentSavings = self.request.get("form_current_savings")

        new_user = money_model.moneyModel(
            price = r_price,
            time = r_time,
            monthlyWage = r_monthly_wage,
            currentSavings = r_currentSavings
            )
        new_user.put()
        self.redirect("/profile")
