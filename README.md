# VisionGuard-AI

VisionGuard-AI is a production-oriented AI CCTV surveillance platform scaffold with:

- FastAPI backend with JWT + RBAC (Super Admin, Security Officer, Viewer)
- Camera onboarding and diagnostics APIs
- Threat event APIs and websocket telemetry
- Next.js + Tailwind dashboard skeleton (camera grid + analytics + event feed)
- PostgreSQL + Redis integration points
- Dockerfiles + Docker Compose deployment
- Beginner-focused docs for installation, troubleshooting, GPU, and camera setup

## Project Structure

```text
visionguard-ai/
├── backend/
├── frontend/
├── ai_models/
├── camera_services/
├── streaming_engine/
├── detection_engines/
├── alerts/
├── recordings/
├── database/
├── docker/
├── deployment/
├── scripts/
├── docs/
├── tests/
├── configs/
└── README.md
```

## Folder Guide

- `backend/`: FastAPI APIs, auth/RBAC, camera/event services, websocket telemetry, SQLAlchemy models.
- `frontend/`: Next.js + Tailwind dashboard (live grid, event panel, analytics panel).
- `ai_models/`: YOLO/FaceNet model weights and TensorRT artifacts.
- `camera_services/`: Vendor-specific camera adapters (RTSP/ONVIF/Xiaomi/Imou/Dahua/etc.).
- `streaming_engine/`: FFmpeg/GStreamer stream and transcode pipeline integrations.
- `detection_engines/`: Threat-detection pipelines (human, fire, smoke, weapon, intrusion).
- `alerts/`: Alert templates and delivery payload structures.
- `recordings/`: Event and continuous recordings (MP4/H264/H265), plus lifecycle cleanup.
- `database/`: DB migrations, seed files, backup/restore scripts.
- `docker/`: Backend/frontend Dockerfiles and Docker Compose stack.
- `deployment/`: Windows/Ubuntu deployment manifests and service configs.
- `scripts/`: Bootstrap scripts for local machine setup.
- `docs/`: Installation, beginner guide, API docs, GPU guide, camera guide, troubleshooting.
- `tests/`: Cross-service and integration test assets.
- `configs/`: Environment examples and runtime configuration templates.

## Quick Start (Local)

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Docker
```bash
cd docker
docker compose up --build
```

## Core Environment Variables

- `APP_NAME`: Display name used by backend service.
- `API_PREFIX`: API base path (default `/api/v1`).
- `SECRET_KEY`: JWT signing key (must be replaced in production).
- `JWT_ALGORITHM`: JWT algorithm (default `HS256`).
- `ACCESS_TOKEN_MINUTES`: Access token expiry in minutes.
- `DATABASE_URL`: SQLAlchemy database connection string.
- `REDIS_URL`: Redis connection string for caching/queue extensions.

## Documentation

- `/docs/installation-guide.md`
- `/docs/beginner-setup-guide.md`
- `/docs/troubleshooting-guide.md`
- `/docs/gpu-setup-guide.md`
- `/docs/camera-setup-guide.md`
- `/docs/api-documentation.md`
