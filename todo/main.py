from fastapi import FastAPI, Request

app = FastAPI(title="Todos")


@app.post('/')
def todo_create(request: Request) -> dict:
    ...


@app.get('/')
def todo_list(request: Request) -> dict:
    ...


@app.get('/{id}')
def todo_get(request: Request, id: int) -> dict:
    ...


@app.put('/{id}')
def todo_update(request: Request, id: int):
    ...


@app.delete('/{id}')
def todo_delete(request: Request, id: int):
    ...
