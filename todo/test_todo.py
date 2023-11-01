import logging

from fastapi import Response
from fastapi.testclient import TestClient

from api.main import app

logging.basicConfig(level=logging.INFO)

client = TestClient(app)

def test_health_check():
    response: Response = client.get('/healthcheck')
    assert response.status_code==200
    assert response.json() == {"status":"ok"}


def test_todo_list():
    response:Response = client.get('/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def todo_create(**created_todo: dict):
    response: Response = client.post('/', json=created_todo)
    data = response.json()
    assert response.status_code == 200
    assert data["id"]
    assert data['title'] == created_todo['title']
    assert data['description'] == created_todo['description']
    assert data['done'] == created_todo['done']


def test_todo_create_done():
    create_data: dict = {
        "title": "Test Title",
        "description": "Test Description",
        "done": True
    }
    todo_create(**create_data)


def test_todo_create_not_done():
    create_data: dict = {
        "title": "Test Title",
        "description": "Test Description",
        "done": False
    }
    todo_create(**create_data)


def todo_get(id: int, get_data: dict):
    response: Response = client.get(f'/{id}')
    data = response.json()
    assert response.status_code == 200
    assert data == get_data


def test_todo_get():
    #  create a todo
    created_todo: dict = {
        "title": "Test Title",
        "description": "Test Description",
        "done": True
    }
    response: Response = client.post('/', json=created_todo)
    data = response.json()
    assert response.status_code == 200
    assert data["id"]
    assert data['title'] == created_todo['title']
    assert data['description'] == created_todo['description']
    assert data['done'] == created_todo['done']

    # get todo
    todo_get(id=data["id"], get_data=data)
