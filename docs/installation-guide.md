# Installation Guide (Windows + Ubuntu)

## 1) Install Python 3.11
- Download from https://www.python.org/downloads/
- Verify: `python --version`

## 2) Install VS Code
- Download from https://code.visualstudio.com/
- Install Python extension.

## 3) Install Git
- Download from https://git-scm.com/downloads
- Verify: `git --version`

## 4) Install FFmpeg
- Ubuntu: `sudo apt install ffmpeg`
- Windows: install from official builds and add to PATH.
- Verify: `ffmpeg -version`

## 5) Install CUDA
- Install NVIDIA drivers first.
- Install CUDA Toolkit from NVIDIA website.
- Verify: `nvidia-smi` and `nvcc --version`

## 6) Install PostgreSQL
- Ubuntu: `sudo apt install postgresql`
- Windows: use official installer.
- Verify connection with `psql`.

## 7) Install Redis
- Ubuntu: `sudo apt install redis`
- Windows: use Docker Redis image.
- Verify: `redis-cli ping`

## 8) Create virtual environment
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
```

## 9) Install dependencies
```bash
pip install -r requirements.txt
```

## 10) Run backend
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 11) Run frontend
```bash
cd frontend
npm install
npm run dev
```

## 12) Connect cameras
- Open API docs at `http://localhost:8000/docs`
- Register/login, then create cameras at `/api/v1/cameras`.

## 13) Run AI detection
- Detection hooks are exposed in backend services; integrate YOLO/TensorRT models in `ai_models/` and `detection_engines/`.

## 14) Use Docker
```bash
cd docker
docker compose up --build
```

## 15) Deploy locally
- Keep backend and frontend as persistent services.
- Use HTTPS reverse proxy in production.
