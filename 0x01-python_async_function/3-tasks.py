#!/usr/bin/env python3
''' A function task_wait_random
    that takes an integer max_delay and returns a asyncio.Task.

    Required: do not create an async function, use
    the regular function syntax to do this. 
'''

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    ''' 
    This calls a randomly generated wait_time 
    function and returns a task

    Args:
        max_delay: Maximum number of seconds function delays

    Return: An asyncio.Task object
    '''
    return asyncio.create_task(wait_random(max_delay))