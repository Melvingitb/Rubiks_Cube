from . import db
from flask_login import UserMixin
from mongoengine import *
import datetime

class User(Document, UserMixin):
    username = StringField(required=True)
    password = StringField(required=True)
    date = DateTimeField(default=datetime.datetime.utcnow)

class Solve(Document):
    time = DecimalField(required=True)
    user = ReferenceField(User)
    plustwo = BooleanField()
    