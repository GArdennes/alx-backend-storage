#!/usr/bin/env python3
"""
Exercise module
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    A simple cache
    """
    def __init__(self) -> None:
        """
        Initialization
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(
            self,
            data: Union[str, bytes, int, float]
            ) -> str:
        """
        Stores data in the cache and returns the generated key
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
