from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.DC

searches = db.searches
