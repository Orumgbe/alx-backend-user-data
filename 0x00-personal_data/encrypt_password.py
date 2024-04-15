#!/usr/bin/env python3
"""This module holds the hash_password method"""
import bcrypt


def hash_password(password: str) -> bytes:
    """This method hashes the user password using bcrypt"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if given password matches hashed password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
