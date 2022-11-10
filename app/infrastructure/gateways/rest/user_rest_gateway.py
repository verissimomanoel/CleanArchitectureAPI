"""Endpoints module."""

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Response, status

from app.infrastructure.containers import Container
from app.core.exeptions.exceptions import NotFoundError
from app.core.use_case.use_case_interfaces import IUserListUseCase, IGetUserByIdUseCase, ICreateUserUseCase, \
    IDeleteUserByIdUseCase

router = APIRouter()


@router.get("/users")
@inject
def get_list(
        user_list_use_case: IUserListUseCase = Depends(Provide[Container.user_list_use_case]),
):
    try:
        return user_list_use_case.execute()
    except Exception as ex:
        print(ex)
        return None


@router.get("/users/{user_id}")
@inject
def get_by_id(
        user_id: int,
        get_user_by_id_use_case: IGetUserByIdUseCase = Depends(Provide[Container.get_user_by_id_use_case]),
):
    try:
        return get_user_by_id_use_case.execute(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/users", status_code=status.HTTP_201_CREATED)
@inject
def add(
        create_user_use_case: ICreateUserUseCase = Depends(Provide[Container.create_user_use_case]),
):
    return create_user_use_case.execute()


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
        user_id: int,
        delete_user_by_id_use_case: IDeleteUserByIdUseCase = Depends(Provide[Container.delete_user_by_id_use_case]),
):
    try:
        delete_user_by_id_use_case.execute(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/status")
def get_status():
    return {"status": "OK"}
