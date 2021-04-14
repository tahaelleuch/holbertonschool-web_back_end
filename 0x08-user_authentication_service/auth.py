#!/usr/bin/env python3
"""Auth module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """crypt password"""
    crypted = bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    )
    return crypted


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """add new user"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError("User " + email + " already exists")
        except NoResultFound:
            pass
        pwd = _hash_password(password)
        new_user = self._db.add_user(email, pwd)
        return new_user

