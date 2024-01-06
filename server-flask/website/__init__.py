from flask import Flask
from dotenv import load_dotenv, find_dotenv
import os
#from pymongo import MongoClient
from flask_pymongo import PyMongo
from mongoengine import *
from flask_login import LoginManager

# finds the .env file
load_dotenv(find_dotenv())

# get the database url from the env file and connects to database with mongoengine
DATABASE_URL = os.environ.get("DATABASE_URL")
conn = connect(host=DATABASE_URL)
db = get_db()
print(db)

#client = MongoClient(DATABASE_URL)

#mongo = PyMongo()

# makes an instance of the app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'CPP Game Dev'
    #app.config['MONGO_DBNAME'] = 'mybrary'
    app.config['MONGO_URI'] = DATABASE_URL

    #mongo.init_app(app)
    #connect(host=DATABASE_URL)

    #db = get_db()
    #print(db)

    #authors = db.authors
    #author_list = authors.find()
    #print(author_list[9])

    #for author in Authors.objects:
    #    print(author.name)

    #authors = Authors._get_collection()
    #author_list = authors.find()
    #print(author_list[9])

    #db = mongo.db
    #authors = db.authors
    #author_list = authors.find()
    #print(author_list[9])

    from .views import views
    from .auth import auth

    from .models import User, Solve

    # lets you manage login functionality with flask login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # define which user is loaded from the database for flask login
    @login_manager.user_loader
    def load_user(id):
        try:
            user = User.objects.get(pk=id)
            print(f'{user.pk} THIS IS THE USER OBJECT!!!')
        except:
            return None
        
        return user

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app