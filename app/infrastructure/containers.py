"""Containers module."""

import pkg_resources
from dependency_injector import containers, providers

from app.core.use_case.use_cases import UserListUseCase
from app.core.use_case.use_cases import GetUserByIdUseCase
from app.core.use_case.use_cases import CreateUserUseCase
from app.core.use_case.use_cases import DeleteUserByIdUseCase
from app.infrastructure.database import Database
from app.infrastructure.repository.repositories import UserSQLiteRepository


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[".external.rest.user_rest_gateway"]
    )

    config = providers.Configuration(yaml_files=[
        pkg_resources.resource_filename(__name__, "../config.yml")
    ])

    db: providers.Singleton[Database] = providers.Singleton(Database, db_url=config.db.url)

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
