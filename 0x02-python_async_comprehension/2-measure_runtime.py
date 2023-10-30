#!/usr/bin/env python3
"""
This run time for four parallel 
comprehensions. 
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    async_comprehension from the previous file and write a measure_runtime     coroutine that will execute async_comprehension four times in parallel     using asyncio.gather.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for s in range(4)))
    return time.perf_counter() - start_time