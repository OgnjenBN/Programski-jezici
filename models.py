from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Roba(Base):
    __tablename__ = 'roba'

    id=Column(Integer, primary_key=True)
    naziv=Column(String(255))
    cijena=Column(Float)
    kolicina=Column(Integer)
    
    
    

