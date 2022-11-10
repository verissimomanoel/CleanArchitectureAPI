"""Containers module."""

from dependency_injector import containers, providers

from app.infrastructure.repository.repositories import UserSQLiteRepository
from app.infrastructure.database import Database
from app.core.use_case.use_cases import UserListUseCase, GetUserByIdUseCase, CreateUserUseCase, DeleteUserByIdUseCase


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

    user_list_use_case = providers.Factory(
        UserListUseCase,
        user_repository=user_repository,
    )

    get_user_by_id_use_case = providers.Factory(
        GetUserByIdUseCase,
        user_repository=user_repository,
    )

    create_user_use_case = providers.Factory(
        CreateUserUseCase,
        user_repository=user_repository,
    )

    delete_user_by_id_use_case = providers.Factory(
        DeleteUserByIdUseCase,
        user_repository=user_repository,
    )
