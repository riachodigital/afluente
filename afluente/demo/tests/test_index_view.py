from os import path

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from afluente.demo.models import Cliente
from afluente.django_assertions import dj_assert_contains


def test_app_link_in_home(client):
    response = client.get('/')
    dj_assert_contains(response, reverse('demo:index'))


IMAGE_PATH = path.dirname(__file__)
IMAGE_PATH = path.join(IMAGE_PATH, 'riachoimg.png')


@pytest.fixture
def demo(db):
    image = SimpleUploadedFile(
        name='riachoimg.png', content=open(IMAGE_PATH, 'rb').read(), content_type='image/png')
    cliente = Cliente(
        nome='Nasa',
        status='INT',
        imagem=image,
        servico='HOSP',
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


def test_img_url(resp, demo):
    cliente = demo[0]
    dj_assert_contains(resp, cliente.imagem.url)
