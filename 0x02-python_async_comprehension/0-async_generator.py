#!/usr/bin/env python3

"""Coroutine that takes no arguments and returns a generator object
that will yield a random number between 0 and 10 every 1 second."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield a random number every 1 second."""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
