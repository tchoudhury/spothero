from sqlalchemy import (
    create_engine,
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from spothero_config.config import SQLALCHEMY_DATABASE_URL

connect_args = {
    'echo': True,
}
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    **connect_args
)
base = declarative_base()
sessionmaker = sessionmaker()
sessionmaker.configure(autocommit=False, autoflush=False, bind=engine)
session = Session(engine)
