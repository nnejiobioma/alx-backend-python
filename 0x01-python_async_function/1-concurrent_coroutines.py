#!/usr/bin/env python3
"""
python file that you’ve written and write 
an async routine called wait_n that takes
in 2 int arguments (in this order) 
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ 
	This Async routine.
        Args:
            max_delay: integer argument.
            n: integer argument.
        Return:
            List of all the delays random float.
    """
    delays: List[float] = []
    new_List: List[float] = []

    for z in range(n):
        delays.append(wait_random(max_delay))

    for s in asyncio.as_completed(delays):
        new_List.append(await s)

    return new_List