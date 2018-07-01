import pytest

from afluente.django_assertions import dj_assert_contains


def test_status_code(client):
    response = client.get('/')
    assert 200 == response.status_code


@pytest.mark.parametrize(
    'content', [
        'Afluente',
        'Home',
        'Contato',
        'Demo',
        'Sobre'
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
        'Isaac',
        'Python Pro',
        'Riacho',
        'CRM',
        'Clientes',
        'Gerenciamento'
    ]
)
def test_contato(client, content):
    response = client.get('/contato/')
    dj_assert_contains(response, content)
