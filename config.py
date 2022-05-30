import os

class Config:
    # app config
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # db config
    MONGO_DB = os.environ.get('MONGO_DB')
    MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
    MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
    MONGO_CLUSTER = os.environ.get('MONGO_CLUSTER')
    MONGO_CLUSTER_ID = os.environ.get('MONGO_CLUSTER_ID')
    MONGO_URI = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}.{MONGO_CLUSTER_ID}.mongodb.net/{MONGO_DB}?retryWrites=true&w=majority"
