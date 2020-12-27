import time
import os
from flask import Flask, render_template, request, redirect
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

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        make_sure_folder_to_save_exists()

        uploaded_file = get_uploaded_file(request)
        uploaded_filename = get_secure_filename_from_file(uploaded_file)
        uploaded_file_extentsion = get_file_extension_from_name(uploaded_filename)

        # Saves file in current directory/ instance / upload_files / secured_filename
        uploaded_file.save(os.path.join(app.instance_path, 'upload_files', uploaded_filename))

        return redirect(request.referrer)


def make_sure_folder_to_save_exists():
    os.makedirs(os.path.join(app.instance_path, 'upload_files'), exist_ok=True)

def get_uploaded_file(request):
    return request.files['file']

def get_secure_filename_from_file(file):
    return secure_filename(file.filename)

def get_file_extension_from_name(filename):
    return os.path.splitext(filename)[-1]