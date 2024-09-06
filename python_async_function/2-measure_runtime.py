#!/usr/bin/env python3


"""Measure the runtime"""
import time
import importlib

wait_n = importlib.import_module("1-concurrent_coroutines").wait_n
"""
import time module
import the concurrent_coroutines module
import the wait_n function
"""


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime

    Args:
    n (int): Number of times to spawn wait_random
    max_delay (int): Maximum delay for each wait_random call

    Returns:
    float: total_time / n
    """
    start = time.perf_counter()
    await wait_n(n, max_delay)
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
