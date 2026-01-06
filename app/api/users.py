from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.users import UsersRepository
from app.schema.users import UsersResponse, UserSearchRequest, DeleteUserResponse
from app.services.users_service import UsersService

router = APIRouter()

async def get_users_service(session: AsyncSession = Depends(get_session)):
    users_repo = UsersRepository(session)
    return UsersService(users_repo, session)

@router.get('/me', response_model=UsersResponse)
async def get_users_by_username(username: str, service: UsersService = Depends(get_users_service)):
    return await service.get_user_by_username(username)




@router.post('/me', response_model=UsersResponse)
async def create_user(username: str, service: UsersService = Depends(get_users_service)):
    return await service.create_user(username)

@router.patch('/me', response_model=UsersResponse)
async def update_user(username: str, new_username: str ,service: UsersService = Depends(get_users_service)):
    return await service.update_username(username, new_username)

@router.delete('/me', response_model=DeleteUserResponse)
async def delete_user(username: str, service: UsersService = Depends(get_users_service)):
    return await service.delete_user(username)

@router.get('/search', response_model=list[UsersResponse])
async def search_user(params: UserSearchRequest = Depends(), service: UsersService = Depends(get_users_service)):
    return await service.search_username(params.query, params.limit, params.offset)