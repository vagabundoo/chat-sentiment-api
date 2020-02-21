from flask import Flask, request
from pymongo import MongoClient
from bson.json_util import dumps
import mongodb as mdb

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
    user_id = mdb.addUser_toDB(username)
    resp = str(f'Created user: {username}, with id {user_id}')
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
    if request.method == 'GET':
        users = str(request.args.get('list_users'))
        participants = users.split(",")
        chat_id = mdb.createChat_toDB(participants)
        resp = f'Created chat with users <b>{", ".join(participants)}</b>, with id {chat_id}'
        print(resp)
        return resp 
    request.post()

@app.route('/chat/<chat_id>/adduser')
def addUsertoChat(user_id):
    pass


#@app.route('/chat/<chat_id>/addmessage')
#def addMessagetoChat(chat_id):

app.run("0.0.0.0", 5002, debug=True)
