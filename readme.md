# Rest-API in Flask

## API:
- An interface you can make a request to and get a response from.

## Rest-API:
- Representational State Transfer API.
- Create Update Retrieve and Delete resources
- Is stateless; doesn't remember what was previously asked (requested).

## Resource:
- A resource is an object that the API stores.
- Multiple resources = Collection

## HTTP Requests:
- Requests are made via HTTP
- GET: retreive info (view collection)
  - Is an idempotent request; can make the same request multiple times without changing anything in the database.
- POST: create a new resource; is not idempotent, because once we send information, we create a new item in the db.
- DELETE: delete resources: is idempotent, we can send the same delete multiple times without side-effects.

## Run API
```t
git clone https://github.com/sele14/flask-restapi

# Build docker image
docker build -t rest-api
# Run
docker run -p 8050:8050 rest-api
```

## Use API

To get all instruments:
``` curl http://127.0.0.1:5000/instruments```


To get an instrument by ID:
```curl http://127.0.0.1:5000/instruments/<string:instrument_id>```

For example, get the first instrument:
```curl http://127.0.0.1:5000/instruments/instrument0```

Delete an instrument:
```curl http://localhost:5000/instruments/instrument2 -X DELETE -v```


Add a new instrument:

```json
body = {
 	"ID" : 2,
 	"Type" : "Cryptocurrency",
 	"Name" : "BTC",
 	"Price" : 27303.96,
 	"Quantity" : 1
}
```
