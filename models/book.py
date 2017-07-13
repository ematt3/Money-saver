from google.appengine.ext import ndb

class Book(ndb.Model):
    author = ndb.StringProperty()
    title = ndb.StringProperty()
    description = ndb.StringProperty()
