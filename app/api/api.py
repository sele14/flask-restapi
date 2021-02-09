from flask_restful import Resource, abort
import logging as logger


INSTRUMENTS = {
	"instrument1" : {
		"ID" : "0",
		"Type" : "Stock",
		"Name" : "ATVI",
		"Price" : 92.68,
		"Quantity" : 5
	},
	"instrument2" : {
		"ID" : "1",
		"Type" : "Bond",
		"Name" : "TNX",
		"Price" : 11.39,
		"Quantity" : 3
	},
	# 'instrument3' : {
	# 	"ID" : "2",
	# 	"Type" : "Cryptocurrency",
	# 	"Name" : "BTC",
	# 	"Price" : 27303.96,
	# 	"Quantity" : 1
	# },
}

def check_if_exists(instrument_id):
    """
    Checks if the instrument exists
    """
    if instrument_id not in INSTRUMENTS:
        abort(404, message=f"Instrument {instrument_id} doesn't exist")


# shows a single instrument and lets you delete an instrument
class Instrument(Resource):
	"""
	Define http request methods to interact with the rest api.
	"""
	def get(self, instrument_id):
		logger.info("Calling GET method")
		check_if_exists(instrument_id)
		return INSTRUMENTS[instrument_id]

	def delete(self, instrument_id):
		logger.info("Calling DELETE method")
		check_if_exists(instrument_id)
		del INSTRUMENTS[instrument_id]
		return '', 204
	
	def put(self, instrument_id):
		logger.info("Calling PUT method")
		args = parser.parse_args()
		instrument = {'instrument': args['instrument']}
		INSTRUMENTS[instrument_id] = instrument
		return instrument, 201

class InstrumentList(Resource):
	"""
	Shows a list of all instruments and allows us to POST to add new instruments
	"""
	def get(self):
		return INSTRUMENTS

	def post(self):
		args = parser.parse_args()
		instrument_id = int(max(INSTRUMENTS.keys()).lstrip('instrument')) + 1
		instrument_id = 'instrument%i' % instrument_id
		INSTRUMENTS[instrument_id] = {'instrument' : args['instrument']}

		return INSTRUMENTS[instrument_id], 201
