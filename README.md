# Creating an API from scratch - to analyze chat sentiments

This was a project to create an API from scratch. The API links to a Mongo Database, and stores the input from the GET and POST requets.  
You can make requests to add users and their conversations/chat logs to the DB. The API has the following functions:

### 1. User endpoints

- (GET) `/user/create/<username>`
  - **Purpose:** Creates a user and saves into the DB
  - **Params:** `username` the user name
  - **Returns:** `user_id`
- (GET) `/user/input`
  - **Purpose:** Gives the user a form in html-format, where they can input a username. Creates that user and saves it into the DB.
  - **Returns:** `user_id`

### 2. Chat endpoints:

- (GET) `/chat/create`
  - **Purpose:** Creates a conversation to load messages
  - **Params:** An array of users ids `[user_id]`
  - **Returns:** `chat_id`
- (GET) `/chat/<chat_id>/adduser`
  - **Purpose:** Adds a user to a chat. This is a way to add more users to a chat after it's creation.
  - **Params:** `user_id`
  - **Returns:** `chat_id`
- (POST) `/chat/<chat_id>/addmessage`
  - **Purpose:** Add a message to the conversation. If the user has not been previously added to the chat, it raises an exception.
  - **Params:**
    - `chat_id`: Chat to store message
    - `user_id`: the user that writes the message
    - `text`: Message text
  - **Returns:** `message_id`
- (GET) `/chat/<chat_id>/list`
  - **Purpose:** Get all messages from `chat_id`
  - **Returns:** json array with all messages from this `chat_id`

### 3. Sentiment analysis

Although not fully implemented, the following function gives an analysis of each message in a particular chat, using the Python library NLTK. It analyses whether the message is positive, negative or neutral, and provides a combined score as well.

- (GET) `/chat/<chat_id>/sentiment`
  - **Purpose:** Analyze messages from `chat_id`. Uses the `NLTK` sentiment analysis package for this task
  - **Returns:** json with all sentiments from messages in the chat