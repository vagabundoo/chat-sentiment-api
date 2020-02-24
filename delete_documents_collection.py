from pymongo import MongoClient

client = MongoClient("mongodb://localhost/chat_sentiments")
db = client.get_database()
users_coll = db["users"]
conversations_coll = db["conversations"]

#users_coll.remove()
#conversations_coll.remove()