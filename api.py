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
    return str(user_id)

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
    #request.post()

@app.route('/chat/<chat_id>/adduser')
def addUsertoChat(chat_id):
    user_id = request.args.get('user_id')
    update = addUserToChat_toDB(user_id, chat_id)
    return chat_id


@app.route('/chat/<chat_id>/addmessage', methods=['POST'])
def addMessagetoChat(chat_id):
    user_id = request.args.get('user_id')
    if not mdb.check_if_user_inChat(chat_id, user_id) or not check_if_user_inDB(user_id):
        raise NameError("User not in present in chat")
    data = request.get_json()
    user_id = data["user_id"]
    text = data["text"]
    return addMessageToChat_toDB(chat_id, user_id, text)



app.run("0.0.0.0", 5001, debug=True)
