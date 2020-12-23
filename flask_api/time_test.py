import time
from flask import Flask
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


app = Flask(__name__)


@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/get')
def get():
    users_ref = db.collection(u'users')
    docs = users_ref.stream()
    users_database_dict = {}
    for doc in docs:
        users_database_dict[doc.id] = doc.to_dict()
    print(users_database_dict)
    return users_database_dict