from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models, schemas

router=APIRouter()

@router.get("/roba/", response_model=List[schemas.MyRoba])
def read_device(db: Session = Depends(get_db)):
    return db.query(models.Roba).all()

''''

@router.get("/{roba_id}", response_model=schemas.MyRoba)
def get_read_device(device_type_id: int, db: Session = Depends(get_db)):
    read_device = db.query(models.Roba).filter(models.Roba.id == roba_id).first()
    if not read_device:
        raise HTTPException(status_code=404, detail="Tip uređaja nije pronađen")
    return read_device



@router.post("/", response_model=schemas.MyRoba)
def create_device_type(device_type: schemas.MyRobaCreate, db: Session = Depends(get_db)):
    # Kreiraj SQLAlchemy instancu na osnovu Pydantic modela
    db_device_type = models.Device(
        k_model=device_type.k_model,
        k_methode_type=device_type.k_methode_type,
        k_calibration_metode=device_type.k_calibration_metode,
        k_calibration_component=device_type.k_calibration_component,
        k_note=device_type.k_note,
        k_low_level_detection=device_type.k_low_level_detection,
        k_max_level_detection=device_type.k_max_level_detection,
        k_low_negative_accepted=device_type.k_low_negative_accepted,
    )
    
    # Dodaj instancu u bazu podataka
    db.add(db_device_type)
    db.commit()
    db.refresh(db_device_type)
    
    return db_device_type
    
@router.delete("/{device_type_id}")
def delete_device(device_type_id: int, db: Session = Depends(get_db)):
    db_delete_device = db.query(models.Device).filter(models.Device.id == device_type_id).first()
    if not db_delete_device:
        raise HTTPException(status_code=404, detail="Tip uređaja nije pronađen")
    db.delete(db_delete_device)
    db.commit()
    return {"detail": "Radni nalog je uspešno obrisan"}
'''