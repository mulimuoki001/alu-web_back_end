#!/usr/bin/env python3

"""async generator"""
import asyncio
import random
from typing import Generator

"""Import random and asyncio modules"""


async def async_generator() -> Generator[float, None, None]:
    """
    Async generator
    Lopps 10 times and
    Yields random numbers between 0 and 10

    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
