#!/usr/bin/python3
"""Module for the Flask API"""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route('/')
def home():
    """Route to the home page"""
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """Route to get the list of users"""
    return jsonify([key for key in users])


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
    if not user_data:
        return jsonify({"error": "Username is required"}), 400
    if "username" not in user_data:
        return jsonify({"error": "Username is required"}), 400

    username = user_data["username"]
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


"""run the flask app"""
if __name__ == "__main__":
    app.run()
