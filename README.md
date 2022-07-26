# Spothero Rates #

## How To Build/Run ##

This is a python based app using pip as the dependency manager, Pytest for testing, SQlite is used for DB portability, and alembic for database migration.
In order to run python tests go to the module you would like to test such as spothero_database/tests and run pytest test_{FILENAME_HERE}.
To build the app you can either run locally or on docker. 

For local you will need to run:
1) pip install -r requirements.txt (located at root directory).
2) go to spothero_alembic and run alembic upgrade head (alembic should get installed via pip)
3) finally run the app by going to spothero_api/Lib/flask and running python app.py

For docker:
1) run docker-compose up from root of directory this will run all the necessary commands and start the app for you.
2) Just as a notice the app should be accessible from outside of the container at localhost:5000/ but if you are 
on windows there may be an issue where you cannot reach it. If this is the case you will need to view the api from 
within the container. To enter container run the following command:
3) docker exec -it {CONTAINER_ID} bash



## Documentation ##

The system is annotated to generate swagger docs automatically. The resulting json is saved to the folder `/resources/swagger.json`, but you can also access a webpage version on `localhost:5000/swagger`.
If you prefer to use the documentation here. The endpoints that are available are the following:

- GET / PUT (localhost:5000/rates):
    get request takes in no query params or payload and will return all available rates in the database. 
    Response will be either 200 or 404 depending on if rates are found.
    put request will take a payload with the following data:
        "{"days": "thurs,fri", "times": "2200-2300", "tz": "America/Chicago", "price": 1400}"
    when entering a timezone the put request will always adjust the timezone to be in accordance with "America/Chicago"
    the response can vary depending on input. Response will be 409 if a rate fails to create 
    (mostly due to enforced DB constraint violation) or a 201 for successful creation

- GET (localhost:5000/api/prices):
  get request takes query params: start and end to form a date range.
  Times are adjusted to the "America/Chicago" timezone.
  Response will vary depending on query param input.
  400 if input doesn't match an enforced schema (The input is not a date)
  or if the input results in either multiple rates returned or spans
  multiple days.
  The response will be 200 if the input is correct.


## Database And Cache ##

For portability purposes sqlite is used to store the data in a file. The file itself can be viewed using sqlite cmd or a sqlite browser.
I prioritized query speed by applying data massaging on insertion. This allowed for rate data to be stored in an optimal manner. For
instance the dates are converted to be stored in the same format as the query params for "/price" endpoint.
For further speed increases using redis or another caching system would be ideal but for ease of use of the application this was not included.
Redis can be used to cache the rates get request as this would not often change unless a new rate is added in which the put request can clear the cache.
Price would also be an optimal target for caching as rates can be cached for a day and then cleared due to the nature of the time range of rates.


## Design And Assumptions ##

Per the requirements, when the system starts a json file located in `resources/data/rates.json` is loaded to the DB.

The requirements also mention that both the rates and the requests for prices can be in any timezone, this can pose a problem as a user can request a day
in one timezone but get rates for a different day in the normalized "America/Chicago" timezone. I took the approach of having one standardized timezone in the DB itself
but any timezone is accepted, it will simply get converted. The system can get a request that once converted results in a time range spanning multiple days, resulting in a 400 error.
This would be an issue for the frontend to solve if we had one, alerting the user of timezone changes.
