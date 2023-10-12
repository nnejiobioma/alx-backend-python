#!/usr/bin/env python3
import time
import asyncio
from concurrent_coroutines import wait_n  # Import the wait_n function directly

def measure_time(n: int, max_delay: float) -> float:
    """Measure the execution time for wait_n.

    Args:
        n (int): The number of calls to wait_n.
        max_delay (float): The maximum delay for each call.

    Returns:
        float: The average execution time per call.
    """
    total_elapsed = 0.0
    for _ in range(n):
        start_time = time.perf_counter()
        asyncio.run(wait_n(1, max_delay))
        end_time = time.perf_counter()
        total_elapsed += end_time - start_time
    return total_elapsed / n