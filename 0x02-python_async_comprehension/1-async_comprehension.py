#!/usr/bin/env python3

"""Coroutine that takes no arguments and returns a generator object"""

from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async comprehensing over async_generator"""
    list_comprehension = [i async for i in async_generator()]
    return list_comprehension
