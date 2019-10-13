import os
from flask import Flask, jsonify
from os.path import join,dirname
from dotenv import load_dotenv
from database import MSSql as Database

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
db = Database(
    server=os.environ.get('DB_SERVER'),
    driver=os.environ.get('DB_DRIVER'),
    password=os.environ.get('DB_PASS'),
    uid=os.environ.get('DB_USER'),
    database=os.environ.get('DB_TITLE')
    )

@app.route('/login')
def hello():
    return jsonify({'title':'Welcome to the login page'})

if __name__ == '__main__':
    app.run()