from sqlalchemy.orm import sessionmaker
from dbConfiguration.Database import engine

session = sessionmaker(bind=engine, autoflush=False, autocommit=False)