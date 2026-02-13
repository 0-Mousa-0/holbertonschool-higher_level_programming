#!/usr/bin/python3
"""first use of framework flask"""

from flask import Flask
from flask import jsonify, request

app = Flask(__name__)
users = {}
@app.route('/')
def home():
    return 'Welcome to the Flask API!'
@app.route('/status')
def status():
    return 'ok'
@app.route('/data')
def data():
    return jsonify(list(users.keys()))
@app.route('/users/<username>')
def users(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)
@app.route("/add_user", methods=["POST"])
def add_user():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201




if __name__ == '__main__':
    app.run()