#!/usr/bin/env python3
"""
    function that measures
    total runtime
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measures total execution time """
    start_time = time.time()
    delay = asyncio.run(wait_n(n, max_delay))
    stop_time = time.time()
    total_time = stop_time - start_time

    return total_time / n
