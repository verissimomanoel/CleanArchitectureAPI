"""Repositories module."""
from abc import ABC, abstractmethod
from typing import List

from app.core.domain.user import User


class IUserRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[User]:
        raise NotImplementedError(
            "The method get_all needs to be implemented by all subclasses!"
        )

    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        raise NotImplementedError(
            "The method get_by_id needs to be implemented by all subclasses!"
        )

    @abstractmethod
    def add(self, user: User) -> User:
        raise NotImplementedError(
            "The method add needs to be implemented by all subclasses!"
        )

    @abstractmethod
    def delete_by_id(self, user_id: int) -> None:
        raise NotImplementedError(
            "The method delete_by_id needs to be implemented by all subclasses!"  # noqa E501
        )
