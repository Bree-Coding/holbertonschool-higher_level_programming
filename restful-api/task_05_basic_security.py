#!/usr/bin/python3
"""Module for the Flask API with basic security"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'my_secret_key'
jwt = JWTManager(app)


users = {
    "user1": {"password": generate_password_hash("password"), "role": "user"},
    "admin1": {"password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_auth():
    return jsonify(message="Basic Auth: Access Granted")


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        token = create_access_token(identity=username)
        return jsonify(access_token=token), 200
    return jsonify({"message": "Bad username or password"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_auth():
    return jsonify(message="JWT Auth: Access Granted")


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_route():
    current_user = get_jwt_identity()
    user = users.get(current_user)
    if user and user.get("role") == "admin":
        return jsonify(message="Admin Access: Granted")
    return jsonify({"error": "Admin access required"}), 403


@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({"error": "Token missing or invalid"}), 401


@jwt.invalid_token_loader
def invalid_token_response(callback):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token_response(callback):
    return jsonify({"error": "Token expired"}), 401


@jwt.revoked_token_loader
def revoked_token_response(callback):
    return jsonify({"error": "Token revoked"}), 401


@jwt.needs_fresh_token_loader
def fresh_token_response(callback):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
