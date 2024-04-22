#!/usr/bin/env python3
"""API authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Manages basic authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks for authentication"""
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path = path + '/'
        if path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """Manages the authorization in header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Checks for current user"""
        return None
