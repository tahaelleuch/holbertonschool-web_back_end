#!/usr/bin/env python3
"""exercice py"""

import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count calls"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wraper"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """call_history"""
    key = method.__qualname__
    inputs = "".join([key, ":inputs"])
    outputs = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wraper"""
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(result))
        return result
    return wrapper


def replay(method):
    """replay function"""
    key = method.__qualname__
    r = redis.Redis()
    number_calls = r.get(key)

    try:
        number_calls = number_calls.decode('utf-8')
    except Exception:
        number_calls = 0
    print("{} was called {} times:".format(key, number_calls))

    inps = key + ":inputs"
    outs = key + ":outputs"

    inputs = r.lrange(inps, 0, -1)
    outputs = r.lrange(outs, 0, -1)
    for inp, out in zip(inputs, outputs):
        inp = inp.decode("utf-8")
        out = out.decode("utf-8")
        print("{}(*{}) -> {}".format(key, inp, out))


class Cache:
    """cashe class"""

    def __init__(self):
        """init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """get"""
        val = self._redis.get(key)
        if fn is None:
            return val
        else:
            fn(val)

    def get_str(self, key):
        """  str get """
        return self.get(key, str)

    def get_int(self, key):
        """  int get """
        return self.get(key, int)
