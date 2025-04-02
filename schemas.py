from pydantic import BaseModel
from typing import Optional


class MyRoba(BaseModel):
    id: int 
    naziv: Optional [str]
    cijena:Optional [float]
    kolicina:Optional [int]
   

class MyRobaCreate(MyRoba):
    pass