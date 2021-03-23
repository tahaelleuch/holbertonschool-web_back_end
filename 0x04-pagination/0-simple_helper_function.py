#!/usr/bin/env python3
"""0-simple_helper_function.py"""


def index_range(page, page_size):
    """
    index of the page

    Args:
        page(int): the number of the page
        page_size(int): the size of the page

    Returns:
        Tuple: first and last index
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
