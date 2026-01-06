from dbConfiguration.Base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Analysis(Base):
    __tablename__ = 'analysis'

    _id: Mapped[str] = mapped_column(primary_key=True)