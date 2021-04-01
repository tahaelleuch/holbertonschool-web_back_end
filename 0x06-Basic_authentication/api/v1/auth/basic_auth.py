#!/usr/bin/env python3
"""
basic auth
"""

from api.v1.auth.auth import Auth
import base64


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
