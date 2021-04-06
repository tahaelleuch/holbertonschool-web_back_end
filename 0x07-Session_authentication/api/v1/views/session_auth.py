#!/usr/bin/env python3
"""session"""

from api.v1.views import app_views
from flask import request, jsonify
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def check_auth() -> str:
    """login"""
    email = request.form.get("email")
    if not email or email == '':
        return jsonify({"error": "email missing"}), 400

    pwd = request.form.get("password")
    if not pwd or pwd == '':
        return jsonify({"error": "password missing"}), 400

    my_user = User().search({"email": email})
    if my_user == []:
        return jsonify({"error": "no user found for this email"}), 404

    if not my_user[0].is_valid_password(pwd):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(my_user[0].id)
    out = jsonify(my_user[0].to_json())
    out.set_cookie(os.getenv("SESSION_NAME"), session_id)
    return out
