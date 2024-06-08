import os
from flask import Flask, flash, request, redirect, url_for, jsonify, make_response, render_template

UPLOAD_FOLDER = './files'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            response = jsonify(msg="No file part")
            return response, 400
        file = request.files['file']
        if file.filename == '':
            response = jsonify(msg="No file provided")
            return response, 400
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            response = jsonify(msg="Fine")
            return response, 200
        response = jsonify(msg="Unsupported ext")
        return response, 400
    response = make_response(render_template("index.html"))
    return response