# Afluente
[![codecov](https://codecov.io/gh/yzakius/afluente/branch/master/graph/badge.svg)](https://codecov.io/gh/yzakius/afluente)

## Sobre

Afluente é um projeto pessoal que visa me auxiliar na gestão de clientes da empresa [Riacho](http://riacho.info). A sua origem surge como um método para para treinar conceitos aprendidos no curso de Python/Django do [Python Pro](http://www.python.pro.br/). Hoje, prentendo reutilizar este projeto para treinar minhas habilidades em frontend (HTML, CSS e JS).

## Objetivos do Projeto

* Gerenciamento de Clientes
* Movimentação Financeira

## Estado Atual do Projeto

Foi retomado o projeto e sendo feitos alguns ajustes.


## Instalação

### Clonando o Repositório

```bash
git clone https://github.com/riachodigital/afluente.git
```

### Configurando o Ambiente

```bash
poetry install
```
Caso queira usar o PIP:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```
Copie o exemplo de varíaveis de ambiente:

```bash
cp contrib/env-sample .env
```

### Rodando o Projeto
```bash
python manage.py migrate
```
```bash
python manage.py runserver
```
