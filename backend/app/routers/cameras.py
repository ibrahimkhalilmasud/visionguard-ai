from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import Camera, Role, User
from ..schemas import CameraCreate, CameraOut
from ..security import require_role
from ..services.camera_manager import UniversalCameraManager

router = APIRouter(prefix="/cameras", tags=["cameras"])
manager = UniversalCameraManager()


@router.get("", response_model=list[CameraOut])
def list_cameras(
    db: Session = Depends(get_db),
    _user: User = Depends(require_role(Role.super_admin, Role.security_officer, Role.viewer)),
):
    return db.query(Camera).all()


@router.post("", response_model=CameraOut, status_code=201)
def create_camera(
    payload: CameraCreate,
    db: Session = Depends(get_db),
    _user: User = Depends(require_role(Role.super_admin, Role.security_officer)),
):
    if payload.protocol.lower() not in manager.supported_protocols:
        raise HTTPException(status_code=400, detail="Unsupported protocol")
    camera = Camera(**payload.model_dump())
    db.add(camera)
    db.commit()
    db.refresh(camera)
    return camera


@router.get("/{camera_id}/diagnostics")
def camera_diagnostics(
    camera_id: int,
    db: Session = Depends(get_db),
    _user: User = Depends(require_role(Role.super_admin, Role.security_officer, Role.viewer)),
):
    camera = db.query(Camera).filter(Camera.id == camera_id).first()
    if not camera:
        raise HTTPException(status_code=404, detail="Camera not found")
    health = manager.test_stream(camera.source)
    if health.reachable:
        camera.last_seen = datetime.utcnow()
        camera.fps = health.fps
        db.add(camera)
        db.commit()
    return {
        "camera_id": camera.id,
        "reachable": health.reachable,
        "fps": health.fps,
        "message": health.message,
        "health": manager.health_status(camera.last_seen),
    }
