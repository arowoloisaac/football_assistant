from dbConfiguration.Database import engine
from dbConfiguration.Base import Base
from models.User import User
from models.Analysis import Analysis

Base().metadata.create_all(engine)