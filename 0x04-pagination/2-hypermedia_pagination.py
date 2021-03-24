#!/usr/bin/env python3
"""0-simple_helper_function.py"""

import csv
import math
from typing import List, Dict


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get the page
        """
        assert type(page) == int
        assert page > 0
        assert type(page_size) == int
        assert page_size > 0
        tup = index_range(page, page_size)
        mydata = self.dataset()
        return mydata[tup[0]:tup[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, str]:
        """get hyper
        """
        dict = {}
        dict["page_size"] = page_size
        dict["page"] = page
        dict["data"] = self.get_page(page, page_size)
        all_pages = math.ceil(len(self.dataset()) / page_size)
        if page + 1 < all_pages:
            dict["next_page"] = page + 1
        else:
            dict["next_page"] = None
        if page - 1 > 0:
            dict["prev_page"] = page - 1
        else:
            dict["prev_page"] = None
        dict["total_pages"] = all_pages
        return dict
