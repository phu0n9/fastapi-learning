from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.users import UsersRepository
from app.schema.users import UsersResponse
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

