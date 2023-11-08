#!/usr/bin/env python3
"""Module holds Auth class"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Manage API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if path requires authentication"""
        if path and path[-1] != '/':
            path = path + '/'
        if path is None or excluded_paths is None:
            return True
        if len(excluded_paths) == 0:
            return True
        if path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """returns None for now"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None for now"""
        return None
