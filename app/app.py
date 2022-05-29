from flask import Flask
from flask_pymongo import PyMongo
from config import Config
mongodb = PyMongo()

def create_app():
    app = Flask(__name__)
    
    # app configuration
    app.config.from_object(Config)

    # init modules
    mongodb.init_app(app)
    
    from .api.api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app