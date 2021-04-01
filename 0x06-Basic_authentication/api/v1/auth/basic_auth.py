#!/usr/bin/env python3
"""
basic auth
"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    BasicAuth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        extract
        Args:
            authorization_header(string): the authorization_heade
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None

        if len(authorization_header) < 7 \
                or authorization_header[:6] != "Basic ":
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """
        Decoded
        Args:
            base64_authorization_header(string): decoded
        """

        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded = base64_authorization_header.encode('utf-8')
            return base64.b64decode(decoded).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """
        extract credentials
        """
        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        credentials = decoded_base64_authorization_header.split(':')

        return (credentials[0], credentials[1])

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd:
                                     str) -> TypeVar('User'):
        """
        user object from credntials
        """
        if not user_email or not isinstance(user_email, str):
            return None

        if not user_pwd or not isinstance(user_pwd, str):
            return None

        try:
            my_user = User.search({'email': user_email})
            if not my_user:
                return None
        except Exception:
            return None

        for one_user in my_user:
            if one_user.is_valid_password(user_pwd):
                return one_user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        get the user
        """
        auth_header = self.authorization_header(request)
        extracted = self.extract_base64_authorization_header(auth_header)
        decoded = self.decode_base64_authorization_header(extracted)
        user_info = self.extract_user_credentials(decoded)
        my_user = self.user_object_from_credentials(user_info[0], user_info[1])
        return my_user
