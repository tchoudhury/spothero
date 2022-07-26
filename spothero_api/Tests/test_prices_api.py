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


def test_get_price_response_200(client):

    url = "/rates"
    query_params = "?start=2015-07-01T07:00:00-05:00&end=2015-07-01T12:00:00-05:00"

    response = client.get(url + query_params)
    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_get_price_invalid_request_args(client):

    url = "/rates"
    query_params = "?startEEEEE=2015-07-01T07:00:00-05:00&endEEEEEEE=2015-07-01T12:00:00-05:00"

    response = client.get(url + query_params)
    assert response.status_code == 400


def test_get_price_multiple_day_range(client):

    url = "/rates"
    query_params = "?start=2015-07-01T07:00:00-05:00&end=2015-07-02T12:00:00-05:00"

    response = client.get(url + query_params)
    assert response.status_code == 400


def test_get_price_multiple_rates_returned(client):

    url = "/rates"
    query_params = "?start=2015-07-01T07:00:00-05:00&end=2015-07-01T22:00:00-05:00"

    response = client.get(url + query_params)
    assert response.status_code == 400
