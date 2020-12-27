import time
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import firebase_admin
from firebase_admin import credentials, firestore


cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "/uploads"


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

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        f = request.files['file']
        os.makedirs(os.path.join(app.instance_path, 'upload_files'), exist_ok=True)
        f.save(os.path.join(app.instance_path, 'upload_files', secure_filename(f.filename)))
        return 'file uploaded successfully'