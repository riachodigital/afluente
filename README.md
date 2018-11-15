# Afluente
[![Build Status](https://travis-ci.org/yzakius/afluente.svg?branch=master)](https://travis-ci.org/yzakius/afluente)
[![Updates](https://pyup.io/repos/github/yzakius/afluente/shield.svg)](https://pyup.io/repos/github/yzakius/afluente/)
[![Python 3](https://pyup.io/repos/github/yzakius/afluente/python-3-shield.svg)](https://pyup.io/repos/github/yzakius/afluente/)
[![codecov](https://codecov.io/gh/yzakius/afluente/branch/master/graph/badge.svg)](https://codecov.io/gh/yzakius/afluente)

## Sobre

Afluente é um projeto pessoal criado para treinar conceitos aprendidos no curso de Python/Django do [Python Pro](http://www.python.pro.br/).

Este projeto visa resolver alguns problemas de gerenciamento administrativo da [Riacho](http://riacho.info), como:

* Gerenciamento de Clientes
* Movimentação Financeira

## Estado Atual do Projeto

No momento o Afluente conta com um app que faz o gerenciamento de clientes. Este recurso está em constante desenvolvimento.

### Roadmap

Criação do app para movimentação financeira.


## Instalação

O Afluente é *suportado pelo Python 3 e Django 2*

### Clonando o Repositório

```console
git clone https://github.com/yzakius/afluente.git
```

### Configurando o Ambiente

*dentro do diretório afluente:*

```console
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
```

### Rodando o Projeto

*dentro do diretório afluente:*

```commandline
python manage.py runserver
```