"""Containers module."""

from dependency_injector import containers, providers

from .database import Database
from app.infrastructure.repository.repositories import UserSQLiteRepository
from app.core.service.services import UserService
from .use_case.use_cases import UserListUseCase


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=["..infrastructure.gateways.rest.user_rest_gateway"]
    )

    config = providers.Configuration(yaml_files=["config.yml"])

    db = providers.Singleton(Database, db_url=config.db.url)

    user_repository = providers.Factory(
        UserSQLiteRepository,
        session_factory=db.provided.session,
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )

    user_list_use_case = providers.Factory(
        UserListUseCase,
        user_repository=user_repository,
    )
