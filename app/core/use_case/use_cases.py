from abc import ABC, abstractmethod
from typing import Iterator

from app.core.models import User
from app.core.repository.repositories import IUserRepository
from app.core.use_case.use_case_interfaces import IUserListUseCase


class UserListUseCase(IUserListUseCase):
    def __init__(self, user_repository: IUserRepository) -> None:
        super(UserListUseCase, self).__init__(user_repository)

    def get_users(self) -> Iterator[User]:
        return self._repository.get_all()