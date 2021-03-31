#!/usr/bin/env python3
"""
Module of authentification
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Class of auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require auth
        Args:
            path(string): the path
            excluded_paths(list of string): exluded path
        Returns:
            False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        header auth
        Args:
            request: the flask request
        Returns:
            None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        currecnt user
        Args:
            request: the flask request
        Returns:
            None
        """
