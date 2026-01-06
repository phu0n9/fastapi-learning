from sqlalchemy import select

from app.models import Tickets
from app.repositories.base import BaseRepository
from app.schema.tickets import TicketsSearchRequest

class TicketRepository(BaseRepository):
    async def get_tickets_by_title(self, params: TicketsSearchRequest) -> list[Tickets]:
        stmt = (
            select(Tickets)
            .where(Tickets.title.ilike(f'%{params.query}%'))
            .limit(params.limit)
            .offset(offset=params.offset)
            .order_by(Tickets.created_at.desc())
        )
        result = await self.session.execute(stmt)
        return list(result.scalars().all())