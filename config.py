import os

class Config:
    # app config
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # db config
    MONGO_DB = os.environ.get('MONGO_DB')
    MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
    MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
    MONGO_URI = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@cluster0.8njfgac.mongodb.net/{MONGO_DB}?retryWrites=true&w=majority"
