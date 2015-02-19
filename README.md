# Luiza labs

Django + Django Rest Framework = <3

# Procedimentos para rodar o projeto

## Instalar os pacotes necessários

    pip install -r requirements.txt

## Criar o banco de dados

    ./manage.py migrate

## Rodar o servidor

    ./manage.py runserver

# Testando o projeto

    ./manage.py test fbusers

# CURL

## Criar

    curl -X POST -F facebookId=1439785724 http://localhost:8000/person/

## Deletar

    curl -X DELETE http://localhost:8000/person/1439785724/


## Listar

    curl http://localhost:8000/person/?limit=xxx


