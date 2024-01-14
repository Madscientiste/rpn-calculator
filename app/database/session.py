from sqlalchemy.orm import sessionmaker
from .base import engine

DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
