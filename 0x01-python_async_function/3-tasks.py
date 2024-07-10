#!/usr/bin/python3
"""
   asyncio
"""

from asyncio import Task, create_task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ function returns a asynchronous type """
    task = create_task(wait_random(max_delay))

    return task
