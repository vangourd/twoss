import os
from flask import Flask, jsonify
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import check_password_hash, generate_password_hash
from os.path import join,dirname
from dotenv import load_dotenv
from database import MSSql as Database
from models import WorkOrder

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('APP_KEY')
db = Database(
    server=os.environ.get('DB_SERVER'),
    driver=os.environ.get('DB_DRIVER'),
    password=os.environ.get('DB_PASS'),
    uid=os.environ.get('DB_USER'),
    database=os.environ.get('DB_TITLE')
    )

class User(object):
    def __init__(self, id ,username, hash):
        self.id = id
        self.username = username
        self.hash = hash
    
    def __str__(self):
        return "User(id='%s')" % self.id

users = [
    User(1, 'blogan',generate_password_hash("abcdefg"))
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username,password):
    user = username_table.get(username)
    if user and check_password_hash(user.hash, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id)

jwt = JWT(app, authenticate, identity)

@app.route('/workorders')
@jwt_required()
def hello():
    wo = WorkOrder(db)
    return jsonify(wo.newest(200))

if __name__ == '__main__':
    app.run()