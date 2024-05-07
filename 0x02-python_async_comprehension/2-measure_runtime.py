#!/usr/bin/env python

"""Measure the runtime of async_comprehension four times in parallel using"""

import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of async_comprehension four times in 
    parallel using asyncio.gather"""

    start_time = time.perf_counter()
    list_comprehension = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*list_comprehension)
    end_time = time.perf_counter()
    return end_time - start_time
