#!/usr/bin/env python3
"""
expiration date for session
"""

from api.v1.auth.session_auth import SessionAuth
import os
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """expired session"""

    def __init__(self):
        """init"""
        if not os.getenv('SESSION_DURATION'):
            self.session_duration = 0
        else:
            try:
                self.session_duration = int(os.getenv('SESSION_DURATION'))
            except Exception:
                self.session_duration = 0

    def create_session(self, user_id=None):
        """create session"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {}
        session_dictionary["user_id"] = user_id
        session_dictionary["created_at"] = datetime.now()
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """user"""
        if session_id is None:
            return None

        if session_id not in self.user_id_by_session_id:
            return None

        session_dict = self.user_id_by_session_id[session_id]

        if self.session_duration <= 0:
            return session_dict["user_id"]

        if "created_at" not in session_dict:
            return None
        t = timedelta(seconds=self.session_duration)
        delta_time = t + session_dict["created_at"]

        if delta_time < datetime.now():
            return None
        return session_dict["user_id"]
