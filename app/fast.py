from fastapi import FastAPI, Query
from sqlalchemy import create_engine, Column, Integer, String, select, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
import psycopg2
import uvicorn
from pydantic import BaseModel
from http import HTTPStatus


DataBase_URL= "postgresql://postgres:postgres@localhost:5432/users"
engine = create_engine(DataBase_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__= 'client'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birthday = Column(String(10), nullable=False)
    gender = Column(String(10), nullable=False)
    mail = Column(String(120), unique=True, nullable=False)
    login = Column(String(50), unique=True, nullable=False)
    password = Column(String(200), nullable=False)


class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    room_quantity = Column(Integer, nullable=False)
    stars = Column(Integer, nullable=False)
    has_spa = Column(Boolean, nullable=False)
    has_swimming_pool= Column(Boolean, nullable=False)
    






app = FastAPI()

class HotelSearchRequest(BaseModel):
    city: str
    guests: int
    date_to: str
    date_for: str


@app.get("/get_user")
def get_users():
    with SessionLocal() as session:
        return session.query(User).all()
    

#@app.get("/get_hotel")
#def get_hotel():
    #with SessionLocal() as session:
        #return session.query(Hotel).all()


@app.post("/get_hotel")
def get_hotel(request: HotelSearchRequest):
    with SessionLocal as session:
        if request.guests < 0:
            return {"status": "NotFound"}, 404
        if request.city.strip():
            return {"status": "NotFound"}, 404
        return session.query(Hotel).all(), 200

        
    


    

if __name__ == '__main__':
    uvicorn.run("fast:app", reload=True)