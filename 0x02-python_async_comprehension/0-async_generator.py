#!/usr/bin/env python3
"""
defines a coroutine which takes no arguments
"""

import asyncio
import random


async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
