import os
from pymongo import MongoClient

db = None

def connect_to_database():
    global db
    if db is None:
        host = os.environ.get("MONGODB_HOST")
        port = int(os.environ.get("MONGODB_PORT"))

        client = MongoClient(host, port)

        db_name = os.environ.get("MONGODB_DB_NAME")
        db = client[db_name]


def get_database():
    global db
    if db is None:
        connect_to_database()
    return db