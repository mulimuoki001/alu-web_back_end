#!/usr/bin/env python3
"""Encrypt password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hash password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
