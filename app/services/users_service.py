from app.exceptions import UserAlreadyExists, UserNotFound
from app.repositories.users import UsersRepository
from app.models import Users
from app.schema.users import DeleteUserResponse

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

    async def update_username(self, username: str, new_username: str) -> Users | None:
        existing_user = await self.users_repo.update_username(username, new_username)
        if not existing_user:
            raise UserNotFound(username)
        return existing_user

    async def delete_user(self, username: str) -> DeleteUserResponse:
        is_deleted = await self.users_repo.delete_username(username)
        if not is_deleted:
            raise UserNotFound(username)
        return DeleteUserResponse(is_deleted=True)

    async def search_username(self, username: str, limit: int = 10, offset: int = 0) -> list[Users]:
        user = await self.users_repo.search_username(username, limit, offset)
        if not user:
            raise UserNotFound(username)
        return user