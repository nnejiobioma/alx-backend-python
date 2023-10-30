#!/usr/bin/env python3
"""
This helps to Calculate the execution
time of 1 co-routine function
"""

import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """Measure the execution time for wait_n.

    Args:
        n (int): The number of calls to wait_n.
        max_delay (float): The maximum delay for each call.

    Returns:
        float: The average execution time per call.
    """

    elapsed_time: float

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time / n