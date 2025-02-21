#!/usr/bin/python3
"""Module for the Flask API"""
from flask import Flask, jsonify, request

"""Initialize the Flask application"""
app = Flask(__name__)


"""Dictionary to store users data"""
users = {}


@app.route('/')
def home():
    """Route to the home page"""
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """Route to get the list of users"""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Route to get the status of the API"""
    return "OK"


@app.route('/users/<username>')
def user(username):
    """Route to get the data about specific user by username"""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404
 

@app.route('/add_user', methods=['POST'])
def add_user():
    """Route to add a new user"""
    user_data = request.get_json()
    if username not in user_data:
        return jsonify({"error": "Username is required"}), 400
    if not username:
        return jsonify({"error": "Username is required"}), 400
    username = user_data.get('username')
    return jsonify({"message": "User added", "user": users[username]}), 201


"""run the flask app"""
if __name__ == "__main__":
    app.run()
