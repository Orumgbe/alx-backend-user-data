#!/usr/bin/env python3
"""Basic Authentication"""
from api.v1.auth.auth import Auth
import base64


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
