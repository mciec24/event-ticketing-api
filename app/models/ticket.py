from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)
    barcode = Column(String, unique=True,  nullable=False)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable =False)

    owner = relationship("User", back_populates="tickets")
    event = relationship("Event", back_populates="tickets")