#!/usr/bin/env python3


"""Basic async syntax example"""
import random

"""import the random library"""


async def wait_random(max_delay: int = 10) -> float:
    """returns the float of a random delay"""
    return random.uniform(0, max_delay)
