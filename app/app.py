from flask import Flask
from flask_restful import reqparse, Api, Resource
import logging as logger
from api.api import INSTRUMENTS, Instrument, InstrumentList

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('instrument')

# Adding the API resource routing
api.add_resource(InstrumentList, '/instruments')
api.add_resource(Instrument, '/instruments/<instrument_id>')

if __name__ == '__main__':
    app.run(debug=True)