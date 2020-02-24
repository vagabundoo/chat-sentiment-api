from pymongo import MongoClient
from bson.objectid import ObjectId
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from json import dumps

client = MongoClient("mongodb://localhost/chat_sentiments")
db = client.get_database()
users_coll = db["users"]
conversations_coll = db["conversations"]

sia = SentimentIntensityAnalyzer()

def getSentimentMessage(message_text):
    return dumps(sia.polarity_scores(message_text))

def getMessageText_byId(msg_id):
    finding = conversations_coll.find_one({"messages.message_id":msg_id}, projection={"_id":0, "messages":1})
    msg = [e for e in finding['messages'] if e["message_id"] == msg_id][0]
    return msg['text']

