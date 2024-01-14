from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from .base import Base
from .session import DBSession


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

    @classmethod
    def get_by_expression(cls, expression: str):
        """
        Get an operation by its expression.

        Parameters:
            expression (str): The mathematical expression.
        """
        with DBSession() as db:
            operation = db.query(cls).filter(cls.expression == expression).first()
            return operation
