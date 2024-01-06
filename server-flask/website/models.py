from . import db
from flask_login import UserMixin
from mongoengine import *

class User(Document, UserMixin):
    username = StringField()