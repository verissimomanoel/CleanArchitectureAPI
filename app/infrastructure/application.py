"""Application module."""

from fastapi import FastAPI

from app.infrastructure.containers import Container
from app.infrastructure.database import Database
from app.infrastructure.external.rest import user_rest_gateway


def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container # type: ignore[attr-defined]
    app.include_router(user_rest_gateway.router)
    return app


app = create_app()
