from pymongo import MongoClient

uri = "mongodb://root:example@mongo:27017"
client = MongoClient(uri)

print(client.list_database_names())