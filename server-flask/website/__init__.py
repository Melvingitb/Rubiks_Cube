from flask import Flask
from dotenv import load_dotenv, find_dotenv
import os
#from pymongo import MongoClient
from flask_pymongo import PyMongo
load_dotenv(find_dotenv())

DATABASE_URL = os.environ.get("DATABASE_URL")
#client = MongoClient(DATABASE_URL)

mongo = PyMongo()

# makes an instance of the app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'CPP Game Dev'
    #app.config['MONGO_DBNAME'] = 'mybrary'
    app.config['MONGO_URI'] = DATABASE_URL
    mongo.init_app(app)

    #db = mongo.db
    #authors = db.authors
    #author_list = authors.find()
    #print(author_list[9])

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app