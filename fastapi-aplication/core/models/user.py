from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class User(BaseModel):
    username: Mapped[str] = mapped_column(unique=True)
    tg_id: Mapped[int] = mapped_column(BigInteger(), unique=True)
