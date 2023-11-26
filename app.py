from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['apartment']
users_collection = db['users']


@app.route('/users', methods=['GET'])
def get_users():
    users = list(users_collection.find({}, {'_id': 0}))
    return jsonify(users)


@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    users_collection.insert_one(new_user)
    return jsonify({'message': 'User created successfully'}), 201


if __name__ == '__main__':
    app.run(port=5000)
