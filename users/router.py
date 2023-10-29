from fastapi import APIRouter

router = APIRouter()

@router.get('/info')
def user_info():
    ...

@router.post("/login")
def user_login():
    ...

@router.post("/register")
def user_register():
    ...

@router.get("/me")
def user_me():
    ...

@router.put('/token/new')
def user_get_token():
    ...

@router.put('/token/refresh')
def user_get_token():
    ...

@router.put('/password/forgot')
def user_password_forgot():
    ...

@router.put('/password/change')
def user_password_change():
    ...