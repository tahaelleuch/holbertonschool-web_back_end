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
        if path is None:
            return True
        if excluded_paths is None and not excluded_paths:
            return True

        if path[-1] != "/":
            path = path + "/"

        if path in excluded_paths:
            return False

        return True

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
