from flask import Flask, request
from pymongo import MongoClient
import random

app = Flask(__name__)

client = MongoClient("mongodb://localhost/chat_sentiments")
db = client.get_database()
users_coll = db["users"]
conversations_coll = db["conversations"]

# (GET) /user/create/<username>
# Purpose: Create a user and save into DB
# Params: username the user name
# Returns: user_id

users_coll.remove({})
#id_number = 1a

@app.route('/user/create/<username>')
def addUser(username):
    """
    Creates a user and saves it into the DB users.
    Args
        username: the username you want to add
    Returns:
        string with username and user_id
    """
    user_id = random.choice(range(1000))
    user = {"user_id": user_id,"username": username}
    users_coll.insert_one(user)
    return f'Created user {username} with user_id: {user_id}'
    # Could consider adding a way to check that the user_id has not been used before.
    #user_id)

(GET) /chat/create
Purpose: Create a conversation to load messages
Params: An array of users ids [user_id]
Returns: chat_id

@app.route('/chat/create')
def createChat(list_users):
    participants = [e for e in user_id]
    conversations_coll.insert_one


app.run("0.0.0.0", 5000, debug=True)
