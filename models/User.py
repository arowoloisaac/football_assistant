from typing import List
from dbConfiguration.Base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.Analysis import Analysis


class User(Base):
    __tablename__ = 'user'

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)

    analyses: Mapped[List[Analysis]] = relationship(back_populates="user")