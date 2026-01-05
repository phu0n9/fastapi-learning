from app.repositories.base import BaseRepository
from app.models import Users
from sqlalchemy import select

class UsersRepository(BaseRepository):
    async def get_user_by_username(self, username: str) -> Users | None:
        result = await self.session.execute(select(Users).where(Users.username == username))
        return result.scalars().one_or_none()

    async def add_new_user(self, username: str) -> Users:
        user = Users(username=username)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user