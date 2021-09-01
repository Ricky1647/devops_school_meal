from flask import Flask, render_template
from flask import Flask, request, jsonify
import os
from flask import send_from_directory
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def predict():
    # initialize the data dictionary that will be returned from the
    # view
    data = {'success': False}
    print('request') 
    # ensure an image was properly uploaded to our endpoint
    if request.method == "GET":
        return '''<!doctype html>
        <link rel="icon" href="data:,">
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <p><input type=file name=image>
        <input type=submit value=Upload>
        </form>'''
if __name__ == '__main__':
    app.run()