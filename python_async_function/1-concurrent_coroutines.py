#!/usr/bin/env python3

"""
Concurrent Coroutines
"""
import asyncio
import random
from typing import List
import heapq
from 0-basic_async_syntax import wait_random

"""
import the random and asyncio libraries
from the 0-basic_async_syntax module
from the typing library import the List module
from the heapq library import the heapq module
import the wait_random function
"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return the list of delays in ascending order.

    Args:
    n (int): Number of times to spawn wait_random
    max_delay (int): Maximum delay for each wait_random call

    Returns:
    List[float]: List of delays in ascending order
    """
    # Create a list to store the tasks
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Use asyncio.gather to run the tasks concurrently and get the results
    results = await asyncio.gather(*tasks)

    # Use a heap to sort the results in ascending order without using sort()

    heapq.heapify(results)

    # Return the sorted list of delays
    return [heapq.heappop(results) for _ in range(n)]
