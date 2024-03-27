#!/usr/bin/env python3
"""
Exercise module
"""
import redis
import uuid
from typing import Union, Optional, Callable


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

    def get(
            self,
            key: str,
            fn: Optional[
                Callable[[bytes], Union[str, int]]
                ] = None
            ) -> Union[str, int, None]:
        """
        Converts data back to the desired format
        using the provided function.

        Args:
            key: The key to retrieve data for.
            fn: An optional function to convert the
            retrieved value.

        Returns:
            The retrieved data converted to the desired
            format (if a converter is provided),
            otherwise the raw bytes, or None
            if the key doesn't exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None

        if fn:
            return fn(data)
        else:
            return data.decode("utf-8")

    def get_str(self, key: str) -> str:
        """
        Parametrizes get with string conversion
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Parametrizes get with integer conversion
        """
        return self.get(key, int)
