from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId

client = MongoClient("mongodb://localhost/chat_sentiments")
db = client.get_database()
users_coll = db["users"]
conversations_coll = db["conversations"]

# User functions

def addUser_toDB(username):
    """Adds user to mongoDB with given username, returns user_id."""
    user = {"username": username}
    insertion = users_coll.insert_one(user)
    return insertion.inserted_id

# Chat functions

def check_if_user_inDB(user_id):
    try:
        users_coll.find_one({"_id": ObjectId(f"{user_id}")})
        return True
    except (InvalidId, NameError):
        return False

def createChat_toDB(user_ids):
    for e in user_ids:
        if not check_if_user_inDB(e):
            raise InvalidId("User ID not in database")
    chat = conversations_coll.insert_one({"participants":list(user_ids)})
    return chat.inserted_id

def addUsertoChat_toDB():
    pass




#addUser_toDB()

# print(createChat_toDB(["bread", "cattle"]))

# from bson.objectid import ObjectId

# users_coll.find_one({"_id": ObjectId("5e4ed27c9aecb4edb7b45299")})