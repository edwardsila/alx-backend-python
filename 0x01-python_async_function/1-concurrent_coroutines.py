#!/usr/bin/env python3
""" async function """

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum number of seconds to wait.

    Returns:
        List[float]: List of all delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

        """ Insert delay into the correct position to maintain sorted order"""
        i = len(delays) - 1
        while i > 0 and delays[i] < delays[i - 1]:
            delays[i], delays[i - 1] = delays[i - 1], delays[i]
            i -= 1

    return delays
