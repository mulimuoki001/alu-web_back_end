#!/usr/bin/env python3
"""Encrypt password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hash password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validate password"""
    return bcrypt.checkpw(password.encode(), hashed_password)
