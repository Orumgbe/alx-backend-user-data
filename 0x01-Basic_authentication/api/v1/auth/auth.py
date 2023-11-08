#!/usr/bin/env python3
"""Module holds Auth class"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Manage API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False for now"""
        return False

    def authorization_header(self, request=None) -> str:
        """returns None for now"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None for now"""
        return None
