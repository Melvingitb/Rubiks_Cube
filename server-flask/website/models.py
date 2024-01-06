from . import db
from flask_login import UserMixin
from mongoengine import *
import datetime

# the outline for the user document in MongoDB
# "UserMixin" is required to utilize the objcct in flask_login
class User(Document, UserMixin):
    meta = {'collection' : 'users'}
    username = StringField(required=True)
    password = StringField(required=True)
    date = DateTimeField(default=datetime.datetime.utcnow)

    # Tells flask_login what the identifier of the object is
    def get_id(self):
        return str(self.pk)

# the outline for the solve document in MongoDB
class Solve(Document):
    meta = {'collection' : 'solves'}
    time = DecimalField(required=True)
    scramble = StringField(required=True)
    user = ReferenceField(User)
    plustwo = BooleanField()
    date = DateTimeField(default=datetime.datetime.utcnow)
    