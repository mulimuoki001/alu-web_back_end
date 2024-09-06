#!/usr/bin/env python3

"""measure runtime"""
import time
import importlib
import asyncio

"""import importlib module
import asyncio module
import time"""
async_comprehension = importlib.import_module(
    "1-async_comprehension"
).async_comprehension

"""
import async_comprehension function from 1-async_comprehension file
"""


async def measure_runtime() -> float:
    """
    Return the runtime of the code
    """
    start = time.time()
    gathered = asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    await gathered
    end = time.time()
    return end - start