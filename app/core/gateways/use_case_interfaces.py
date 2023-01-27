from abc import ABC
from typing import Iterator

from app.core.domain.user import User
from app.core.gateways.repositories import IUserRepository


class IUserListUseCase(ABC):
    def __init__(self, user_repository: IUserRepository) -> None:
        self._repository: IUserRepository = user_repository

    def execute(self) -> Iterator[User]:
        raise NotImplementedError(
            "The method execute needs to be implemented by all subclasses!"
        )


class IGetUserByIdUseCase(ABC):
    def __init__(self, user_repository: IUserRepository) -> None:
        self._repository: IUserRepository = user_repository

    def execute(self, user_id: int) -> User:
        raise NotImplementedError(
            "The method execute needs to be implemented by all subclasses!"
        )


class ICreateUserUseCase(ABC):
    def __init__(self, user_repository: IUserRepository) -> None:
        self._repository: IUserRepository = user_repository

    def execute(self) -> User:
        raise NotImplementedError(
            "The method execute needs to be implemented by all subclasses!"
        )


class IDeleteUserByIdUseCase(ABC):
    def __init__(self, user_repository: IUserRepository) -> None:
        self._repository: IUserRepository = user_repository

    def execute(self, user_id: int) -> None:
        raise NotImplementedError(
            "The method execute needs to be implemented by all subclasses!"
        )
