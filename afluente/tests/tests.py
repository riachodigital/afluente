def test_status_code(client):
    response = client.get('/')
    assert 200 == response.status_code
