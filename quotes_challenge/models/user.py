from sqlalchemy import (
    Column,
    Text,
)

from .meta import Base


class User(Base):
    """ The SQLAlchemy declarative model class for a User object. """
    __tablename__ = 'users'
    uuid = Column(Text, primary_key=True)
