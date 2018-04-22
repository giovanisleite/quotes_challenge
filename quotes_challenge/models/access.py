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

    session_uuid = Column(ForeignKey('sessions.uuid'), nullable=False)
    session = relationship('Session', backref='accesses')

    def __json__(self, request):
        return {'page': self.page, 'datetime': self.datetime.isoformat()}

    @classmethod
    def from_json(cls, data):
        return cls(**data)
