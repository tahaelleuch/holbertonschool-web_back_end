#!/usr/bin/env python3
"""web"""

import requests
import redis
from functools import wraps
from typing import Callable

r = redis.Redis()


def count_req(method: Callable) -> Callable:
    """counr request"""
    @wraps(method)
    def wrapper(url):
        """wrapper"""
        r.incr("count:{}".format(url))
        cached_html = r.get("cached:{}".format(url))
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        r.setex("cached:{}".format(url), 10, html)
        return html

    return wrapper


@count_req
def get_page(url: str) -> str:
    """get page"""
    req = requests.get(url)
    return req.text
