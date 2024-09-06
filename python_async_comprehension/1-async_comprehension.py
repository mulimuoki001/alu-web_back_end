#!/usr/bin/env python3

"""async generator"""
import asyncio
from typing import Generator
import importlib

"""
import importlib module
import asyncio module
import Generator module from typing library

"""

async_generator = importlib.import_module("0-async_generator").async_generator
"""The following function stores the first 10 random numbers in a list"""


async def async_comprehension() -> Generator[float, None, None]:
    """The coroutine will collect 10 random numbers
    using an async comprehensing over
    async_generator, then return the 10 random numbers.
    """
    values = async_generator()
    return [value async for value in values]
