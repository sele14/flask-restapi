from flask_restful import Api
from app.main import app

rest_server = Api(app)

class Instruments():

    # define http request methods
    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass
