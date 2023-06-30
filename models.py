from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, engine


class User(Base):
    __tablename__ = "users"

    id= Column(Integer, primary_key=True, index=True, autoincrement=True)
    name= Column(String, unique=False, index=True)
    surname= Column(String, unique=False, index=True)
    age= Column(Integer)
    phone_number= Column(String, unique=True)
    username= Column(String, unique=True, index=True)
    password= Column(String)
    email= Column(String, unique=True, index=True)
    gender= Column(String)
    address= Column(String)

    tickets = relationship("Ticket", back_populates="user")


class Airport(Base):
    __tablename__ = "airports"

    id= Column(Integer, primary_key=True, index=True, autoincrement=True)
    name= Column(String, unique=False, index=True)
    address= Column(String)

class Company(Base):
    __tablename__ = "companies"

    id= Column(Integer, primary_key=True, index=True, autoincrement=True)
    name= Column(String)

    airplanes = relationship("Airplane", back_populates="company")

class Airplane(Base):
    __tablename__ = "airplanes"

    id= Column(Integer, primary_key=True, index=True, autoincrement=True)
    company_id= Column(Integer, ForeignKey(Company.id))
    name= Column(String, unique=False, index=True)
    number_of_sit= Column(Integer)

    flights = relationship("Flight", back_populates="airplane")
    company = relationship("Company", back_populates="airplanes")

class Flight(Base):
    __tablename__ = "flights"

    id= Column(Integer, primary_key=True, index=True, autoincrement=True)
    origin_airport_id= Column(Integer)
    destination_airport_id= Column(Integer)
    takeoff_date= Column(String, unique=False)
    landing_date= Column(String, unique=False)
    airplane_id= Column(Integer, ForeignKey(Airplane.id))
    class_type= Column(String)

    airplane = relationship("Airplane", back_populates="flights")
    tickets = relationship("Ticket", back_populates="flight")

class Ticket(Base):
    __tablename__ = "tickets"

    id= Column(Integer, primary_key=True, index=True, autoincrement=True)
    flight_id= Column(Integer, ForeignKey(Flight.id))
    user_id= Column(Integer, ForeignKey(User.id))
    price= Column(Float)
    sitNumber= Column(Integer)
    type= Column(String)

    flight = relationship("Flight", back_populates="tickets")
    user = relationship("User", back_populates="tickets")



Base.metadata.create_all(bind=engine)