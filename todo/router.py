from fastapi import APIRouter, Request

router = APIRouter()


@router.post('/')
def todo_create(request: Request) -> dict:
    ...


@router.get('/')
def todo_list(request: Request) -> dict:
    ...


@router.get('/{id}')
def todo_get(request: Request, id: int) -> dict:
    ...


@router.put('/{id}')
def todo_update(request: Request, id: int):
    ...


@router.delete('/{id}')
def todo_delete(request: Request, id: int):
    ...
