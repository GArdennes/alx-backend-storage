#!/usr/bin/env python3
"""
Exercise module
"""
import redis
import uuid
from typing import Any, Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    A decorator that counts calls to a method
    and stores the count in Redis.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        Increments the call count for the method
        and calls the original method.
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


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

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in the cache and returns the generated key
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        '''
        Retrieves a value from a Redis data storage.
        '''
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        '''
        Retrieves a string value from a Redis data storage.
        '''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        '''
        Retrieves an integer value from a Redis data storage.
        '''
        return self.get(key, lambda x: int(x))
