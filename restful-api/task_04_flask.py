#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def user(username):
    info = users.get(username)
    if info:
        return jsonify(info)
    else:
        return '"error": "User not found"', 404

@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    username = user_data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    return jsonify({"message": "User added", "user": users[username]})

if __name__ == "__main__": 
    app.run(host="localhost", port=5000)
