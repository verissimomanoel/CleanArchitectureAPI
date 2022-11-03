"""Endpoints module."""

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Response, status

from app.core.containers import Container
from app.core.exeptions.exceptions import NotFoundError
from app.core.service.services import UserService
from app.core.use_case.use_case_interfaces import IUserListUseCase

router = APIRouter()


@router.get("/users")
@inject
def get_list(
        user_list_use_case: IUserListUseCase = Depends(Provide[Container.user_list_use_case]),
):
    try:
        return user_list_use_case.get_users()
    except Exception as ex:
        print(ex)
        return None


@router.get("/users/{user_id}")
@inject
def get_by_id(
        user_id: int,
        user_service: UserService = Depends(Provide[Container.user_service]),
):
    try:
        return user_service.get_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/users", status_code=status.HTTP_201_CREATED)
@inject
def add(
        user_service: UserService = Depends(Provide[Container.user_service]),
):
    return user_service.create_user()


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
        user_id: int,
        user_service: UserService = Depends(Provide[Container.user_service]),
):
    try:
        user_service.delete_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/status")
def get_status():
    return {"status": "OK"}
