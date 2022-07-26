import pytest
from flask import Flask


@pytest.fixture(scope='module')
def client():
    app = Flask(__name__)
    app.testing = True

    # Create a test client using the Flask application configured for testing
    with app.test_client() as client:
        # Establish an application context
        with app.app_context():
            yield client

    return client


def test_get_rates_response(client):

    url = "/rates"

    response = client.get(url)
    assert response.status_code == 200
    assert response.content_type == "application/json"

    ### Need to mock response data and create model.Rates factory. Using this we can test the response body.
    ### With mock data you can use empty records to test for 404.


def test_put_rates_response(client):
    url = "/rates"
    headers = {
        "Accept": 'application/json'
    }
    body = {
        "days": "thurs,fri",
        "times": "2200-2300",
        "tz": "America/Chicago",
        "price": 1400
    }

    response = client.put(url, data=body, headers=headers)
    assert response.content_type == "application/json"
    assert response.json["days"] == "thurs, fri"
    assert response.status_code == 201

    response = client.put(url, data=body, headers=headers)
    assert response.status_code == 409
