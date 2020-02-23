from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId
from bson.json_util import dumps

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

def createChat_toDB(user_ids):
    for e in user_ids:
        if not check_if_user_inDB(e):
            raise InvalidId("User ID not in database")
    chat = conversations_coll.insert_one({"participants":list(user_ids), "messages":[]})
    return chat.inserted_id

def addUserToChat_toDB(user_id, chat_id):
    if not check_if_user_inDB:
        raise NameError("User_ID not in database")
    update = conversations_coll.update_one({"_id": ObjectId(chat_id)}, {"$addToSet":{"participants" : ObjectId(user_id)}})
    return update

def addMessageToChat_toDB(chat_id, user_id, text):
    message = {
        "user_id":user_id,
        "text":text
    } # Consider adding a timestamp to the message as well.
    update = conversations_coll.update_one({"_id": ObjectId(chat_id)}, {"$addToSet":{"messages" : message}})
    return update

# Validation functions

def check_if_user_inDB(user_id):
    try:
        object = users_coll.find_one({"_id": ObjectId(user_id)})
        #print(object)
        return True
    except (InvalidId, NameError):
        return False

def check_if_user_inChat(chat_id, user_id):
    if type(conversations_coll.find_one({"$and": [{"_id":ObjectId(chat_id)},{"participants":ObjectId(user_id)}]})) == dict:
        return True
    return False

#def getAllMessagesChat(chat_id):




