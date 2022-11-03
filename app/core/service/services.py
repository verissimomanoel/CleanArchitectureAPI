"""Services module."""

from typing import Iterator
from uuid import uuid4

from app.core.models import User
from app.core.repository.repositories import IUserRepository


class UserService:

    def __init__(self, user_repository: IUserRepository) -> None:
        self._repository: IUserRepository = user_repository

    def get_user_by_id(self, user_id: int) -> User:
        return self._repository.get_by_id(user_id)

    def create_user(self) -> User:
        uid = uuid4()
        return self._repository.add(email=f"{uid}@email.com", password="pwd")

    def delete_user_by_id(self, user_id: int) -> None:
        return self._repository.delete_by_id(user_id)
