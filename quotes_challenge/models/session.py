from sqlalchemy import (
    Column,
    Text,
)

from .meta import Base


class Session(Base):
    __tablename__ = 'sessions'
    uuid = Column(Text, primary_key=True)

    def __json__(self, request):
        return {'uuid': self.uuid, 'accesses': self.accesses}

    @classmethod
    def from_json(cls, data):
        return cls(**data)
