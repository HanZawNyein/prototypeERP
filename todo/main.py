from fastapi import FastAPI
from .router import router

app = FastAPI(title="Todos")
app.include_router(router)
