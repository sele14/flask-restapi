from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "You Are at Home"

# run app
app.run(host='127.0.0.1', port=8050, debug=True)