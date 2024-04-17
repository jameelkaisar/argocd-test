from flask import Flask, jsonify
from flask_cors import CORS
from time import sleep

app = Flask(__name__)

CORS(app)

@app.route('/')
def get_hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/message')
def get_message():
    return jsonify({'message': 'Booi Kya Karaan Azz Kal?'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
