#!/usr/bin/env python3


import time
import importlib
import asyncio

async_comprehension = importlib.import_module(
    "1-async_comprehension"
).async_comprehension


async def measure_runtime() -> float:
    """Return the runtime of the code"""
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
