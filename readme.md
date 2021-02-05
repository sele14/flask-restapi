# Rest-API:

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
  - Is an idempotent request; can make the same request multiple times wuthout changing anything in the database.
- POST: create a new resource; is not idempotent, because once we send information, we create a new item in the db.
- DELETE: delete resources: is idempotent, we can send the same delete multiple times without side-effects.