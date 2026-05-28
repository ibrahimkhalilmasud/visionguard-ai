from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from .models import Role


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserCreate(BaseModel):
    email: EmailStr
    full_name: str = Field(min_length=2)
    password: str = Field(min_length=8)
    role: Role = Role.viewer


class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    role: Role
    is_active: bool

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class CameraCreate(BaseModel):
    name: str
    source: str
    protocol: str
    location: str | None = None


class CameraOut(BaseModel):
    id: int
    name: str
    source: str
    protocol: str
    location: str | None
    enabled: bool
    fps: float | None

    class Config:
        from_attributes = True


class EventCreate(BaseModel):
    camera_id: int
    threat_type: str
    confidence: float = Field(ge=0, le=1)
    snapshot_path: str | None = None


class EventOut(BaseModel):
    id: int
    camera_id: int
    threat_type: str
    confidence: float
    snapshot_path: str | None
    created_at: datetime

    class Config:
        from_attributes = True
