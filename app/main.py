from flask import Flask
import os
import logging as logger

logger.basicConfig(level='INFO')

app = Flask(__name__)

@app.route("/")
def index():
    return "You Are at Home"


if __name__=="__main__":
    logger.info("Starting the server")
    # run app
    app.run(host='127.0.0.1', port=8050, debug=True)