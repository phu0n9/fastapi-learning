from sqlalchemy import select

from app.models import Chats
from app.repositories.base import BaseRepository

class ChatsRepository(BaseRepository):
    async def get_chat(self, chat_id: int) -> Chats:
        result = await self.session.execute(select(Chats).where(Chats.id == chat_id))
        return result.scalar_one_or_none()

    async def create_chat(self, user_id: int) -> Chats:
        chat = Chats(user_id=user_id)
        self.session.add(chat)
        await self.session.commit()
        await self.session.refresh(chat)
        return chat

