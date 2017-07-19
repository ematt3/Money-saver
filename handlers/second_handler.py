
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
        r_monthlyWage = self.request.get("form_monthlyWage")
        r_currentSavings = self.request.get("form_currentSavings")

        logging.info(r_price)
        logging.info(r_time)
        logging.info(r_monthlyWage)
        logging.info(r_currentSavings)

        new_user = money_model.moneyModel(
            price = float(r_price),
            time = int(r_time),
            monthlyWage = float(r_monthlyWage),
            currentSavings = float(r_currentSavings)
            )

        new_user.put()
        self.redirect("/profile")
