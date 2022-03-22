from unittest.mock import patch

import pytest

from app import create_app

app = create_app() # pylint: disable=invalid-name

@pytest.fixture
def client():
    app.config['TESTING'] = True
    yield app.test_client()

def test_movie_details(mock, client):  # pylint: disable=redefined-outer-name
    """
    Check movie details endpoint
    """
    resp = client.get('/v1/movies/218/details')
    assert resp.status_code == 200
    assert resp.json['title'] == 'The Terminator'
