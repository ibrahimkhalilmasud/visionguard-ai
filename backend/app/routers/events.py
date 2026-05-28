from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import Camera, Event, Role, User
from ..schemas import EventCreate, EventOut
from ..security import require_role

router = APIRouter(prefix="/events", tags=["events"])


@router.get("", response_model=list[EventOut])
def list_events(
    db: Session = Depends(get_db),
    _user: User = Depends(require_role(Role.super_admin, Role.security_officer, Role.viewer)),
):
    return db.query(Event).order_by(Event.created_at.desc()).limit(200).all()


@router.post("", response_model=EventOut, status_code=201)
def create_event(
    payload: EventCreate,
    db: Session = Depends(get_db),
    _user: User = Depends(require_role(Role.super_admin, Role.security_officer)),
):
    camera = db.query(Camera).filter(Camera.id == payload.camera_id).first()
    if not camera:
        raise HTTPException(status_code=404, detail="Camera not found")
    event = Event(**payload.model_dump())
    db.add(event)
    db.commit()
    db.refresh(event)
    return event
