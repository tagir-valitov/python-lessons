from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, select, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
import psycopg2
import uvicorn
from pydantic import BaseModel
from http import HTTPStatus
from datetime import date


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
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class HotelSearchRequest(BaseModel):
    city: str
    guests: int
    date_from: date
    date_to: date


class HotelResponse(BaseModel):
    name: str
    location: str
    room_quantity: int
    stars: int
    has_spa: bool
    has_swimming_pool: bool


class ListHotels(BaseModel):
    data: list[HotelResponse]
    class Config:
        from_attributes = True
    
@app.get("/get_user")
def get_users():
    with SessionLocal() as session:
        return session.query(User).all()
    

#@app.get("/get_hotel")
#def get_hotel():
    #with SessionLocal() as session:
        #return session.query(Hotel).all()


@app.post("/check_hotel")
def check_hotel(request: HotelSearchRequest):
    if request.guests <= 0:
        return {"status": "NotFound"}, 404
    else:
        return {"status": "Ok"},200
        


@app.get("/get_hotels", response_model=ListHotels)
def get_hotels(request: HotelSearchRequest)-> list[HotelResponse]:
    with SessionLocal() as session:
        city = request.city
        hotels = session.query(Hotel).filter(Hotel.location == city).all()
        if not hotels:
            return {"status": "NotFound"}, 404
        hotel_list = [
            HotelResponse(
                name=hotel.name,
                location=hotel.location,
                room_quantity=hotel.room_quantity,
                stars=hotel.stars,
                has_spa=hotel.has_spa,
                has_swimming_pool=hotel.has_swimming_pool
            ) for hotel in hotels
        ]
        
        return ListHotels(data=hotel_list)

if __name__ == '__main__':
    uvicorn.run("fast:app", reload=True)