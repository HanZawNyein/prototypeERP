from fastapi import FastAPI
from .router import router

app = FastAPI(title="Users")
app.include_router(router)
