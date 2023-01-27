from typing import Iterator
from uuid import uuid4

from app.core.domain.user import User
from app.core.gateways.repositories import IUserRepository
from app.core.gateways.use_case_interfaces import IUserListUseCase
from app.core.gateways.use_case_interfaces import IGetUserByIdUseCase
from app.core.gateways.use_case_interfaces import ICreateUserUseCase
from app.core.gateways.use_case_interfaces import IDeleteUserByIdUseCase


class UserListUseCase(IUserListUseCase):
    def __init__(self, user_repository: IUserRepository) -> None:
        super(UserListUseCase, self).__init__(user_repository)

    def execute(self) -> Iterator[User]:
        return self._repository.get_all()


class GetUserByIdUseCase(IGetUserByIdUseCase):
    def __init__(self, user_repository: IUserRepository) -> None:
        super(GetUserByIdUseCase, self).__init__(user_repository)

    def execute(self, user_id: int) -> User:
        return self._repository.get_by_id(user_id)


class CreateUserUseCase(ICreateUserUseCase):
    def __init__(self, user_repository: IUserRepository) -> None:
        super(CreateUserUseCase, self).__init__(user_repository)

    def execute(self) -> User:
        uid = uuid4()
        user = User(
            id=None,
            is_active=None,
            email=f"{uid}@email.com",
            password="pwd"
        )
        return self._repository.add(user)


class DeleteUserByIdUseCase(IDeleteUserByIdUseCase):
    def __init__(self, user_repository: IUserRepository) -> None:
        super(DeleteUserByIdUseCase, self).__init__(user_repository)

    def execute(self, user_id: int) -> None:
        return self._repository.delete_by_id(user_id)
