from sqlalchemy import create_engine

db_url = "dialect+driver://username:password@host:port/database"

engine = create_engine(db_url, pool_pre_ping=True, echo=True)