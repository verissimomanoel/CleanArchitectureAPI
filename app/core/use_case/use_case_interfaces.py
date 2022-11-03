from abc import ABC, abstractmethod
from typing import Iterator

from app.core.models import User
from app.core.repository.repositories import IUserRepository


class IUserListUseCase(ABC):
    def __init__(self, user_repository: IUserRepository) -> None:
        self._repository: IUserRepository = user_repository

    def get_users(self) -> Iterator[User]:
        raise NotImplemented("The method get_users needs to be implemented by all subclasses!")