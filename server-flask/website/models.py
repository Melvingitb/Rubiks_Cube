from . import db
from flask_login import UserMixin
from mongoengine import *
import datetime

class User(Document, UserMixin):
    meta = {'collection' : 'users'}
    username = StringField(required=True)
    password = StringField(required=True)
    date = DateTimeField(default=datetime.datetime.utcnow)

    def get_id(self):
        return str(self.pk)

class Solve(Document):
    meta = {'collection' : 'solves'}
    time = DecimalField(required=True)
    scramble = StringField(required=True)
    user = ReferenceField(User)
    plustwo = BooleanField()
    date = DateTimeField(default=datetime.datetime.utcnow)
    