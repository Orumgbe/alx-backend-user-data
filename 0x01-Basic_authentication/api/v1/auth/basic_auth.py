#!/usr/bin/env python3
"""Basic Authentication"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """Handles basic authentication"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns the Base64 part of the Authorization in header"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split()[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Returns decoded value of Base64 string"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            auth_utf8_enc = base64_authorization_header.encode('utf-8')
            auth_base64_dec = base64.b64decode(auth_utf8_enc)
        except BaseException:
            return None
        return auth_base64_dec.decode('utf-8')

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """Return user email and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if decoded_base64_authorization_header.find(':') == -1:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(":", 1))

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str
                                     ) -> TypeVar('User'):
        """Returns user instance based on email and password"""
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            users = User.search({"email": user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Overloads the auth and retrieves user for a request"""
        user = None
        credentials = self.authorization_header(request)
        if credentials:
            auth_b64 = self.extract_base64_authorization_header(credentials)
            if auth_b64:
                auth_txt = self.decode_base64_authorization_header(auth_b64)
                if auth_txt:
                    username, pwd = self.extract_user_credentials(auth_txt)
                    if username and pwd:
                        user = self.user_object_from_credentials(username, pwd)
        return user
