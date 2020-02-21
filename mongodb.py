from pymongo import MongoClient

client = MongoClient("mongodb://localhost/chat_sentiments")
db = client.get_database()
users_coll = db["users"]
conversations_coll = db["conversations"]

def addUser_toDB(username):
    """Adds user to mongoDB with given username, returns user_id."""
    user = {"username": username}
    insertion = users_coll.insert_one(user)
    return insertion.inserted_id

addUser_toDB('Johnnyyyyy')

#addUser_toDB()