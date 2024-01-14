from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from app.config import SQLITE_PATH


Base = declarative_base()
engine = create_engine(f"sqlite:///{SQLITE_PATH}")
