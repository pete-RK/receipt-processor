from fastapi import FastAPI
from app.routes import router

def create_app():
    app = FastAPI(title="Receipt Processor API")
    app.include_router(router)
    return app