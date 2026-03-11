
# import os
# from dotenv import load_dotenv
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# load_dotenv()

# uri = "mongodb+srv://tnbsoftlab_db_user:" + os.getenv("db_password") + "@cluster0.lz7camk.mongodb.net/?appName=Cluster0"
# print(uri)
# print("Connecting to MongoDB...")
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
# db = client["casino"]
# collection = db["players"]
# collection.insert_one({"name": "herve", "solde": 1000})

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi


load_dotenv()


def _build_uri():
    password = os.getenv("db_password") or os.getenv("DB_PASSWORD")
    if not password:
        return None
    return (
        "mongodb+srv://tnbsoftlab_db_user:"
        + password
        + "@cluster0.lz7camk.mongodb.net/?appName=Cluster0"
    )


def get_players_collection():
    uri = _build_uri()
    if not uri:
        return None
    try:
        client = MongoClient(uri, server_api=ServerApi("1"))
        client.admin.command("ping")
        database = client["casino"]
        return database["players"]
    except Exception:
        return None


def load_player_stats(name_user):
    collection = get_players_collection()
    if collection is None:
        return None
    return collection.find_one({"name": name_user})


def save_player_stats(name_user, stats):
    collection = get_players_collection()
    if collection is None:
        return False
    data_to_save = dict(stats)
    data_to_save["name"] = name_user
    collection.update_one({"name": name_user}, {"$set": data_to_save}, upsert=True)
    return True