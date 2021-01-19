import time
import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

import firebase_admin
from firebase_admin import credentials, firestore, storage

from secrets import STORAGE_BUCKET_ID

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred,{
    'storageBucket': STORAGE_BUCKET_ID
})
db = firestore.client()
bucket = storage.bucket()

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
        userId = request.args.get('user')

        make_sure_folder_to_save_exists()

        uploaded_file = get_uploaded_file(request)
        uploaded_filename = get_secure_filename_from_file(uploaded_file)
        uploaded_file_extentsion = get_file_extension_from_name(uploaded_filename)
        
        if not isCsv(uploaded_file_extentsion):
            return redirect(request.referrer)

        # Saves file in current directory/ instance / upload_files / secured_filename
        full_file_path = os.path.join(app.instance_path, 'upload_files', uploaded_filename)

        uploaded_file.save(full_file_path)

        blob = bucket.blob(userId+"/"+uploaded_filename)

        with open(full_file_path, 'rb') as my_file:
            blob.upload_from_file(my_file)

        return redirect(request.referrer)


def make_sure_folder_to_save_exists():
    os.makedirs(os.path.join(app.instance_path, 'upload_files'), exist_ok=True)

def get_uploaded_file(request):
    return request.files['file']

def get_secure_filename_from_file(file):
    return secure_filename(file.filename)

def get_file_extension_from_name(filename):
    return os.path.splitext(filename)[-1]

def isCsv(file_extension):
    return file_extension == ".csv"