#!/usr/bin/env python3
"""
The basics of async
asynchronous coroutine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    takes in an integer argument (max_delay, with a default
    value of 10) named wait_random that waits for a 
    random delay between 0 and max_delay
    """
    randomValue = random.uniform(0, max_delay)
    await asyncio.sleep(randomValue)
    return randomValue