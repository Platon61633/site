import os
from flask import Flask, flash, request, redirect, url_for, jsonify, make_response, render_template
from entropy import entropy
from info import info

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
            response = make_response(render_template("index.html", msg="No file part", status=0))
            return response, 400
        file = request.files['file']
        if file.filename == '':
            response = make_response(render_template("index.html", msg="No file provided", status=0))
            return response, 400
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            attack_type = entropy(filename)
            data = info(filename)
            response = make_response(render_template("result.html", msg="Success!", data=data, status=1))
            return response, 200
        response = make_response(render_template("index.html", msg="Unsupported ext", status=0))
        return response, 400
    response = make_response(render_template("index.html"))
    return response