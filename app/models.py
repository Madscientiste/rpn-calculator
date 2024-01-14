from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from datetime import datetime

import pathlib

SQLITE_PATH = pathlib.Path(__file__).parent.parent / "database.sqlite"

Base = declarative_base()

engine = create_engine(f"sqlite:///{SQLITE_PATH}")
Base.metadata.create_all(bind=engine)

DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Operation(Base):
    __tablename__ = "operations"

    id = Column(Integer, primary_key=True, index=True)
    expression = Column(String, index=True)
    result = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "expression": self.expression,
            "result": self.result,
            "timestamp": self.timestamp,
        }

    @classmethod
    def create_operation(cls, expression: str, result: int):
        """
        Create a new operation and add it to the database.

        Parameters:
            expression (str): The mathematical expression.
            result (int): The result of the expression.
        """
        with DBSession() as db:
            new_operation = cls(expression=expression, result=result)
            db.add(new_operation)
            db.commit()

    @classmethod
    def get_operations(cls):
        """
        Get all operations from the database.
        """
        with DBSession() as db:
            operations = db.query(cls).all()
            return operations
