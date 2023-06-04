from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from ..database.config import Base


class User(Base):
    __tablename__ = "users"

    id: Column(Integer, primary_key=True, index=True)
    name: Column(String, unique=False, index=True)
    surname: Column(String, unique=False, index=True)
    age: Column(Integer)
    phone_number: Column(Integer, unique=True)
    username: Column(String, unique=True, index=True)
    password: Column(String)
    email: Column(String, unique=True, index=True)
    gender: Column(Boolean)
    address: Column(String)