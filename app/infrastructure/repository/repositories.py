"""Repositories module."""
from contextlib import AbstractContextManager
from typing import Callable, Iterator, List

from sqlalchemy.orm import Session

from app.core.exeptions.exceptions import UserNotFoundError
from app.core.domain.user import User
from app.infrastructure.domain.entities import UserEntity
from app.core.repository.repositories import IUserRepository


class UserSQLiteRepository(IUserRepository):

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[User]:
        with self.session_factory() as session:
            entities = session.query(UserEntity).all()

            return self.__create_user_objects(entities)

    def get_by_id(self, user_id: int) -> User:
        with self.session_factory() as session:
            user_entity: UserEntity = session.query(UserEntity).filter(UserEntity.id == user_id).first()

            if not user_entity:
                raise UserNotFoundError(user_id)

            user = User(
                id=user_entity.id,
                email=user_entity.email,
                password=user_entity.hashed_password,
                is_active=user_entity.is_active
            )

        return user

    def add(self, user: User) -> User:
        with self.session_factory() as session:
            user_entity = UserEntity(
                email=user.email,
                hashed_password=user.password,
                is_active=user.is_active
            )
            session.add(user_entity)
            session.commit()
            session.refresh(user_entity)

            user.id = user_entity.id

        return user

    def delete_by_id(self, user_id: int) -> None:
        with self.session_factory() as session:
            entity: UserEntity = session.query(UserEntity).filter(UserEntity.id == user_id).first()
            if not entity:
                raise UserNotFoundError(user_id)
            session.delete(entity)
            session.commit()

    def __create_user_objects(self, entities: List[UserEntity]):
        return [
            User(
                id=e.id,
                email=e.email,
                password=e.hashed_password,
                is_active=e.is_active
            )
            for e in entities
        ]
