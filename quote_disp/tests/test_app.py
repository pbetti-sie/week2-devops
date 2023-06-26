import json

def test_get_index_route(app, client):
    """
    GIVEN quote display service
    WHEN '/' page is requested (GET)
    THEN check that the index page is displayed
    """
    res = client.get('/')
    assert res.status_code == 200
    assert b"Quote Display Service" in res.data

def test_get_quote_route(app, client):
    """
    GIVEN quote display service
    WHEN '/get_quote' page is requested (GET)
    THEN check that a 500 is returned (backend is down)
    """
    res = client.get('/get_quote')
    assert res.status_code == 500


