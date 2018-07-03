import pytest
from django.urls import reverse

from afluente.demo.models import Cliente
from afluente.django_assertions import dj_assert_contains


def test_app_link_in_home(client):
    response = client.get('/')
    dj_assert_contains(response, reverse('demo:index'))


@pytest.fixture
def demo(db):
    cliente = Cliente(
        nome='Nasa',
        status='Inativo',
        servico='Hospedagem'
    )
    cliente.save()
    return [cliente]


@pytest.fixture
def resp(client, demo):
    return client.get(reverse('demo:index'))


def test_status_code(resp):
    assert 200 == resp.status_code


@pytest.mark.parametrize(
    'content', [
        'Nasa',
        'Inativo',
        'Hospedagem',
    ]
)
def test_demo_index_content(resp, content):
    dj_assert_contains(resp, content)
