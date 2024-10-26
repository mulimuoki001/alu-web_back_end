#!/usr/bin/env python3
"""log stats from collection
"""
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection):
    """script that provides some stats about Nginx logs stored in MongoDB
    """
    result = mongo_collection.count_documents({})
    print(f"{result} logs")
    print("Methods:")
    for method in METHODS:
        value = mongo_collection.count_documents({"method": method})
        print(f"\t{method}: {value}")
    status_check = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"GET /status: {status_check}")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)