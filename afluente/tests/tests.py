import pytest

from afluente.django_assertions import dj_assert_contains


def test_status_code(client):
    response = client.get('/')
    assert 200 == response.status_code


@pytest.mark.parametrize(
    'content', [
        'Afluente',
        'Contato',
        'Demo',
    ]
)
def test_home(client, content):
    response = client.get('/')
    dj_assert_contains(response, content)


def test_contato_status_code(client):
    response = client.get('/contato/')
    assert 200 == response.status_code


@pytest.mark.parametrize(
    'content', [
        'Afluente',
        'Python Pro',
        'Riacho',
        'CRM',
    ]
)
def test_contato(client, content):
    response = client.get('/contato/')
    dj_assert_contains(response, content)
