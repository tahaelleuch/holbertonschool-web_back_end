#!/usr/bin/env python3
"""
basic auth
"""

from api.v1.auth.auth import Auth


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
