#!/usr/bin/env python3
"""
async_generator that takes
no argument
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loops 10 times, wait for 1 seconds
    yield random number between 0 to 10
    """
    for s in range(10):
        await asyncio.sleep(1) # Asynchronously wait for 1 second
        yield random.uniform(0, 10)