from fastapi import FastAPI
from db.database import Base, engine
from api.v1 import users

from models.event import Event
from models.user import User
from models.ticket import Ticket

app = FastAPI(title="Ticket Sale Platform API")

Base.metadata.create_all(bind=engine)

app.include_router(users.router)

@app.get("/")
def get_all():
    return {"message" : "It's working!"}