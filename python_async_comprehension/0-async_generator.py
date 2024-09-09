#!/usr/bin/env python3

"""async generator"""
import random
from typing import List


async def async_generator() -> List[float]:
    """The coroutine will collect 10 random numbers
    using an async comprehensing over
    async_generator, then return the 10 random numbers.
    """
    list1 = [random.random() for _ in range(10)]
    return list1
