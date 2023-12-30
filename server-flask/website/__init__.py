from flask import Flask

# makes an instance of the app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'CPP Game Dev'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app