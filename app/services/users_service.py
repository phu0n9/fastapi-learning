from app.exceptions import UserAlreadyExists, UserNotFound
from app.repositories.users import UsersRepository
from app.models import Users

class UsersService:
    def __init__(self, users_repo: UsersRepository, session):
        self.users_repo = users_repo
        self.session = session

    async def get_user_by_username(self, username: str) -> Users | None:
        user = await self.users_repo.get_user_by_username(username)
        if not user:
            raise UserNotFound(username)
        return user

    async def create_user(self, username: str) -> Users | None:
        existing_user = await self.users_repo.get_user_by_username(username)
        if existing_user:
            raise UserAlreadyExists(username)
        return await self.users_repo.add_new_user(username)