from flask import jsonify, request, make_response, current_app
from flask import Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from bson.objectid import ObjectId

from ..app import mongodb
from .decorators import token_required
from .helpers import validate_email, to_json

api = Blueprint('api_blueprint', __name__)

user_collection = mongodb.db.users
template_collection = mongodb.db.templates

@api.post('/register')
def register():
    data = request.get_json()
    print(data)
    if 'first_name' in data and 'last_name' in data and 'email' in data and 'password' in data:
        if not validate_email(data['email']):
            return jsonify({'error': 'Invalid Email'}), 400

        # User Already Exist 409
        user = user_collection.find_one({'email': data['email']})
        if user:
            return jsonify({'error': 'User Already Exist'}), 409
        
        new_user = {
            "first_name": data['first_name'],
            "last_name": data['last_name'],
            "email": data['email'],
            "password": generate_password_hash(data['password'])}
            
        user_collection.insert_one(new_user)
        return jsonify({'status': 200}), 200

    return jsonify({'status': 'missing parameter'}), 400

@api.post('/login')
def login():
    data = request.get_json()
    if 'email' in data and 'password' in data:
        user = user_collection.find_one({'email': data['email']})
        
        # check for user and password
        if not user:
            return jsonify({'error': 'User Not Found'}), 404
        
        if not check_password_hash(user['password'], data['password']):
            return make_response('Access Denied', 401, {'WWW-Authenticate':'Basic realm="Login Required"'})

        # generate token
        print(str(user.get('_id')))
        token = jwt.encode(
            {
                'id': str(user.get('_id')), 
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=300)
            }, 
            current_app.config['SECRET_KEY'], 
            algorithm="HS256",
            headers={"typ": "Bearer", "alg": "HS256"})
        
        return jsonify({'token': token}), 200
    
    return jsonify({'error': 'missing parameter'}), 400

# Template CRUD

@api.post('/template')
@token_required
def create_template(current_user):
    data = request.get_json()
    if 'template_name' in data and 'subject' in data and 'body' in data:
        author_id = current_user['_id']
        template = {
                "template_name": data["template_name"], 
                "subject": data["subject"], 
                "body": data["body"], 
                "author_id": author_id
            }
        oid = template_collection.insert_one(template).inserted_id
        template['_id'] = str(oid)
        template['author_id'] = str(author_id)
        return jsonify({'status': 'New Template Created', 'template': template}), 200
    
    return jsonify({'error': 'missing parameter'}), 400

@api.get('/template')
@token_required
def templates(current_user):
    templates = []
    author_id = current_user['_id']
    res = template_collection.find({"author_id" : { "$eq" : author_id}})
    for template in res:
        print(template)
        templates.append(to_json(template))
    return jsonify({'templates': templates})

@api.get('/template/<template_id>')
@token_required
def template(current_user, template_id):
    len_tid = len(template_id)
    if (len_tid > 24 or len_tid < 24):
        return jsonify({'error': 'Invalid template_id'}), 400 
    
    oid = ObjectId(template_id)
    template = template_collection.find_one_or_404({"_id": oid})
    if template:
        author_id = str(template['author_id'])
        if str(current_user['_id']) == author_id:
            template_json = to_json(template)
            return jsonify(template_json)

        return jsonify({'error': 'You are not authorized to see this template'}), 403 

@api.put('/template/<template_id>')
@token_required
def update_template(current_user, template_id):
    len_tid = len(template_id)
    if (len_tid > 24 or len_tid < 24):
        return jsonify({'error': 'Invalid template_id'}), 400 

    data = request.get_json()
    if 'template_name' in data or 'subject' in data or 'body' in data:
        oid = ObjectId(template_id)
        template = template_collection.find_one_or_404({"_id": oid})
        if template:
            author_id = str(template['author_id'])
            if str(current_user['_id']) == author_id:
                # check which field need to be change
                accepeted_data = ['template_name', 'subject', 'body']
                new_data = {}
                for k,v in data.items():
                    if k in accepeted_data:
                        new_data[k] = v

                # update template
                template_collection.update_one({'_id': oid}, {"$set": new_data})
                updated_template = template_collection.find_one({"_id": oid})
                return jsonify({'status': 'template updated', 'template': to_json(updated_template)}), 200

            return jsonify({'error': 'You are not authorized to update this template'}), 403 

    return jsonify({'error': 'missing parameter'}), 400
    
@api.delete('/template/<template_id>')
@token_required
def delete_template(current_user, template_id):
    len_tid = len(template_id)
    if (len_tid > 24 or len_tid < 24):
        return jsonify({'error': 'Invalid template_id'}), 400 
        
    oid = ObjectId(template_id)
    template = template_collection.find_one_or_404({"_id": oid})
    if template:
        author_id = str(template['author_id'])
        if str(current_user['_id']) == author_id:
            template_collection.delete_one({'_id': oid})
            return jsonify({'status': 'template deleted'}), 202

        return jsonify({'error': 'You are not authorized to delete this template'}), 403 

@api.app_errorhandler(404)
def handle_404(err):
    return jsonify({'error': 'Not Found'}), 404






