"""Application module."""

from fastapi import FastAPI

from app.core.containers import Container
from app.infrastructure.gateways.rest import user_rest_gateway


def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container
    app.include_router(user_rest_gateway.router)
    return app


app = create_app()
