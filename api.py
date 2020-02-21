from flask import Flask, request
from pymongo import MongoClient
import random
from bson.json_util import dumps

app = Flask(__name__)

client = MongoClient("mongodb://localhost/chat_sentiments")
db = client.get_database()
users_coll = db["users"]
conversations_coll = db["conversations"]

# User creation

@app.route('/user/create/<username>')   
def addUser(username):
    """
    Creates a user and saves it into the DB users.
    Args
        username: the username you want to add
    Returns:
        string with username and user_id
    """
    user = {"username": username}
    result = users_coll.insert_one(user)
    resp = str(f'Created user: {username}, with id {result.inserted_id}')
    print(resp)
    return resp

@app.route('/user/input', methods=['GET', 'POST']) 
def inputUserForm():
    """
    Provides a form in html, where user can submit new users to database
    Returns:
        string with username and user_id
    """
    if request.method == 'POST': #this block is only entered when the form is submitted
        username = request.form.get('username')
        user = {"username": username}
        result = users_coll.insert_one(user)
        resp = str(f'Created user: {username}, with id {result.inserted_id}')
        print(resp)
        return resp 

    return '''<form method="POST">
                  <h3> Provide a username to add to the database: <input type="text" name="username"></h3>
                  <input type="submit" value="Submit"><br>
              </form>'''

# Chats

@app.route('/chat/create/', methods=['GET', 'POST'])
def createChat():
    if request.method == 'GET'
    users = request.args.get('list_users')
    participants = users.split(",")
    result = conversations_coll.insert_one({"participants":participants})
    resp = f'Created chat with users {", ".join(participants)}, with id {result.inserted_id}'
    return resp 


app.run("0.0.0.0", 5002, debug=True)
