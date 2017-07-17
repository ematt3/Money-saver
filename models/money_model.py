from google.appengine.ext import ndb

class moneyModel(ndb.Model):
	user_responses = ndb.StringProperty()
	user_email = ndb.StringProperty()