from django.urls import reverse


def test_status_code(client):
    resp = client.get(reverse('login'))
    assert 200 == resp.status_code
