from fastapi import FastAPI
from .controllers.router import router

app = FastAPI(title="Todo API")
app.include_router(router)
