from dbConfiguration.Database import engine
from dbConfiguration.Base import Base
from models.User import User


Base().metadata.create_all(engine)