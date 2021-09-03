from flask import Flask, render_template
from flask import Flask, request, jsonify
import os
from flask import send_from_directory
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def main():
        return  render_template('index.html')



if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)







"""如果不用render_template跑得出來
def main():
        return '''
        <!doctype html>
        <head>
            <title>Upload new File</title>
        </head>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <p><input type=file name=image>
        <input type=submit value=Upload>
        </form>
        '''
"""



