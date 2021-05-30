#!/usr/bin/env python3
""" log ngnix"""
from pymongo import MongoClient


if __name__ == "__main__":
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    print(str(logs.count_documents({})) + " logs")

    print("Methods:")
    for method in methods:
        count_method = logs.count_documents({'method': method})
        print('\tmethod ' + method + ': ' + str(count_method))

    print("{} status check".format(logs.count_documents({"path": "/status"})))
