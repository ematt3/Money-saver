from google.appengine.ext import ndb

class moneyModel(ndb.Model):

	price = ndb.FloatProperty()
	time = ndb.IntegerProperty()
	monthlyWage = ndb.FloatProperty()
	currentSavings = ndb.FloatProperty()

	user_responses = ndb.StringProperty()
	user_email = ndb.StringProperty()