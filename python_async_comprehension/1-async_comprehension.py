#!/usr/bin/env python3

"""async generator"""
import asyncio
import importlib
from typing import List

"""
import importlib module
import asyncio module
import Generator module from typing library

"""

async_generator = importlib.import_module("0-async_generator").async_generator
"""The following function stores the first 10 random numbers in a list"""


async def async_comprehension() -> List[float]:
    """The coroutine will collect 10 random numbers
    using an async comprehensing over
    async_generator, then return the 10 random numbers.
    """
    list1 = [value async for value in async_generator()]
    return list1
