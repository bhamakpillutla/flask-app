from flask import Flask, jsonify
import time
import logging

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'
if __name__=='__main__':
    app.run(debug=False,host='0.0.0.0', port = 7000)
