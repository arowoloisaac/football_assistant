from sqlalchemy import ForeignKey
from dbConfiguration.Base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.User import User

class Analysis(Base):
    __tablename__ = 'analysis'

    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey('user.id', ondelete="cascade"), nullable=False)

    user: Mapped[User] = relationship("User", back_populates="analyses")
