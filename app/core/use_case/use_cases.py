from typing import Iterator
from uuid import uuid4

from app.core.models import User
from app.core.repository.repositories import IUserRepository
from app.core.use_case.use_case_interfaces import IUserListUseCase, IGetUserByIdUseCase, ICreateUserUseCase, \
    IDeleteUserByIdUseCase


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
        return self._repository.add(email=f"{uid}@email.com", password="pwd")


class DeleteUserByIdUseCase(IDeleteUserByIdUseCase):
    def __init__(self, user_repository: IUserRepository) -> None:
        super(DeleteUserByIdUseCase, self).__init__(user_repository)

    def execute(self, user_id: int) -> None:
        return self._repository.delete_by_id(user_id)
