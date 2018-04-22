from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
    DateTime,
)
from sqlalchemy.orm import relationship

from .meta import Base


class Access(Base):
    """ The SQLAlchemy declarative model class for a Page object. """
    __tablename__ = 'accesses'
    id = Column(Integer, primary_key=True)

    page = Column(Text, nullable=False)
    datetime = Column(DateTime, nullable=False)

    user_uuid = Column(ForeignKey('users.uuid'), nullable=False)
    user = relationship('User', backref='accesses')
