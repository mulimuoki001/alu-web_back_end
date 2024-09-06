#!/usr/bin/env python3


    """
    A normal function that returns a coroutine object
    """
import asyncio
import importlib
wait_random = importlib.import_module("0-basic_async_syntax").wait_random
"""
import the random and asyncio libraries
from the 0-basic_async_syntax module
import wait_random function
"""

def task_wait_random(max_delay: int):
    """
    returns the float of a random delay
    """
    return asyncio.Task
