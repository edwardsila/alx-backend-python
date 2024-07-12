#!/usr/bin/env python3
"""
runtime for four paralle comprehesion
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure the runtime """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4))
    stop_time = time.time()
    return stop_time - start_time
