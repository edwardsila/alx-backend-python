#!/usr/bin/env python3
"""
async comprehension
"""
from typing import list
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ async def """
    value = [i async for i in async_generator()]
    return value
