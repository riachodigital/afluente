import pytest
from django.urls import reverse

from afluente.django_assertions import dj_assert_contains


def test_app_link_in_home(client):
    response = client.get('/')
    dj_assert_contains(response, reverse('demo:index'))


def test_status_code(client):
    response = client.get(reverse('demo:index'))
    assert 200 == response.status_code


@pytest.mark.parametrize(
    'content', [
        'Usuario',
        'Senha',
        'Demo',
        'CRM',
        'Riacho',
        'Logar',
    ]
)
def test_demo(client, content):
    response = client.get('/demo/')
    dj_assert_contains(response, reverse('demo:index'))
