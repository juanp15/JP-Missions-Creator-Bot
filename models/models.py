from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass

Base = declarative_base()

@dataclass
class Mission(Base):
    __tablename__ = "missions"
    
    message_id = Column(String(20), primary_key=True)
    channel_id = Column(String(20), nullable=False)
    imgs_ids = Column(String(255), nullable=True)
    members = relationship("Member", back_populates="mission")

@dataclass
class Member(Base):
    __tablename__ = "members"

    id = Column(String(36), primary_key=True)
    mission_id = Column(String(20), ForeignKey('missions.message_id'), nullable=False)
    user_id = Column(String(20), nullable=False)
    class_ = Column(String(10), nullable=False)
    aircraft = Column(String(35), nullable=False)
    mission = relationship("Mission", back_populates="members")
