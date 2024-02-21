from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['mydatabase']

collection = db["test_collection"]

document = {"name": "Prajval"}
collection.insert_one(document)