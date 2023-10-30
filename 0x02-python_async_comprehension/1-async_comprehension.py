#!/usr/bin/env python3
"""
async_generator that takes
argument
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 randon number using async 
    comprehention over async_generator
    returns 10 random numbers.
    """
    return [s async for s in async_generator()]
