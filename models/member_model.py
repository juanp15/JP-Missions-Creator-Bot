from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass
from config.db import engine

Base = declarative_base()

@dataclass
class Member(Base):
    __tablename__ = "members"

    id = Column(String(36), primary_key=True)
    mission_id = Column(String(20), ForeignKey('missions.message_id'), nullable=False)
    user_id = Column(String(20), nullable=False)
    class_ = Column(String(10), nullable=False)
    aircraft = Column(String(35), nullable=False)
    mission = relationship("Mission", back_populates="members")

Base.metadata.create_all(engine)
