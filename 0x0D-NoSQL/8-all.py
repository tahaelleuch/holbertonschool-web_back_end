#!/usr/bin/env python3
""" 8-all"""


def list_all(mongo_collection):
    """list_all"""
    return mongo_collection.find()
