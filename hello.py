from flask import Flask, render_template, request, send_file
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/images', methods=['POST'])
def submit_image():
    file = request.files['file']
    if file.filename != "":
        return send_file(BytesIO(file.read()), file.mimetype)
    else:
        return "no image submitted"
