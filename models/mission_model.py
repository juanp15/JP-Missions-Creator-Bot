from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass
from config.db import engine

Base = declarative_base()

@dataclass
class Mission(Base):
    __tablename__ = "missions"
    
    message_id = Column(String(20), primary_key=True)
    channel_id = Column(String(20), nullable=False)
    imgs_ids = Column(String(255), nullable=True)
    members = relationship("Member", back_populates="mission")

Base.metadata.create_all(engine)
