from flask import request, jsonify, current_app
from ..app import mongodb
from bson.objectid import ObjectId
import jwt
from functools import wraps

user_collection = mongodb.db.users

def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({'error': 'Token Missing'}), 401
        
        try:
            token = token.replace("Bearer ","")
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms="HS256")
            current_user = user_collection.find_one({'_id': ObjectId(data['id'])})
        except Exception as e:
            print(e)
            return jsonify({'error': 'Invalid Token'}), 401
        
        return f(current_user, *args, **kwargs)

    return wrapper
