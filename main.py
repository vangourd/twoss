from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/login')
def hello():
    return jsonify({'title':'Welcome to the login page'})

if __name__ == '__main__':
    app.run()