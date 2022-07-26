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
            yield client  # this is where the testing happens!
