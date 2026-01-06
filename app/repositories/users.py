from app.repositories.base import BaseRepository
from app.models import Users
from sqlalchemy import select, delete, update

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

    async def update_username(self, username: str, new_username: str) -> Users | None:
        stmt = (update(Users).where(Users.username == username).values(username=new_username).returning(Users))
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalars().one_or_none()

    async def delete_username(self, username: str) -> bool:
        stmt = delete(Users).where(Users.username == username)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0

    async def search_username(self, query: str, limit: int = 10, offset: int = 0) -> list[Users]:
        stmt = (select(Users).where(Users.username.ilike(f'%{query}%')).limit(limit).offset(offset).order_by(Users.username))
        result = await self.session.execute(stmt)
        return list(result.scalars().all())