import typing
import enum

from sqlalchemy import Enum
from advanced_alchemy.base import orm_registry, BigIntAuditBase
from sqlalchemy import orm
import sqlalchemy as sa

METADATA: typing.Final = orm_registry.metadata
orm.DeclarativeBase.metadata = METADATA

class Issues(enum.Enum):
    WRONG_REFERENCE = 1
    BAD_PROMPT = 2
    UI_ERROR = 3
    OTHER_ERROR = 4


class Status(enum.Enum):
    OPEN = 1
    IN_PROGRESS = 2
    RESOLVED = 3

class Users(BigIntAuditBase):
    __tablename__ = 'users'
    username: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    is_deleted: orm.Mapped[bool] = orm.mapped_column(sa.Boolean, nullable=False, default=False)

class Messages(BigIntAuditBase):
    __tablename__ = 'messages'
    chat_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey('chats.id'))
    ai_response: orm.Mapped[str] = orm.mapped_column(sa.Text, nullable=False)
    user_message: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)


class Chats(BigIntAuditBase):
    __tablename__ = 'chats'
    user_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("users.id"))
    messages: orm.Mapped[list[Messages]] = orm.relationship("Messages", lazy="selectin", uselist=True)


class Tickets(BigIntAuditBase):
    __tablename__ = 'tickets'
    message_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("messages.id"))
    title: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    issue_type: orm.Mapped[Issues] = orm.mapped_column(Enum(Issues), nullable=False, default=Issues.OTHER_ERROR)
    status: orm.Mapped[Status] = orm.mapped_column(Enum(Status), nullable=False, default=Status.OPEN)
    is_deleted: orm.Mapped[bool] = orm.mapped_column(sa.Boolean, nullable=False)