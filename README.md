# VisionGuard-AI

VisionGuard-AI is a smart CCTV app.
It has:
- **Backend** (API server)
- **Frontend** (web dashboard)
- **Docker option** (run everything together)

---

## Super Simple Setup (Copy + Paste)

## Option A (Easiest): Run with Docker

### 1) Install Docker Desktop
- Download: https://www.docker.com/products/docker-desktop/
- Open Docker Desktop and keep it running.

### 2) Run the project
```bash
cd /tmp/workspace/ibrahimkhalilmasud/visionguard-ai/docker
docker compose up --build
```

### 3) Open the app
- Frontend: `http://localhost:3000`
- Backend API docs: `http://localhost:8000/docs`

If Docker fails, use **Option B** below.

---

## Option B: Run Backend + Frontend Manually

## What you need first
Install these:
- Python 3.11+
- Node.js 18+
- Git

Check versions:
```bash
python --version
node --version
git --version
```

---

## Step 1) Start Backend

```bash
cd /tmp/workspace/ibrahimkhalilmasud/visionguard-ai/backend
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Windows activation command (use this instead of `source`):
```powershell
.venv\Scripts\activate
```

When backend is running, open: `http://localhost:8000/docs`

---

## Step 2) Start Frontend (new terminal)

```bash
cd /tmp/workspace/ibrahimkhalilmasud/visionguard-ai/frontend
npm install
npm run dev
```

Open: `http://localhost:3000`

---

## First Time Use
1. Open backend docs: `http://localhost:8000/docs`
2. Register/login
3. Add camera with `/api/v1/cameras`
4. Open dashboard at `http://localhost:3000`

---

## If Something Breaks (Quick Fixes)

## 1) `python: command not found`
Try:
```bash
python3 --version
```
Then replace `python` with `python3` in commands.

On Windows, you can also try:
```powershell
py --version
```

## 2) `pip: command not found`
Use:
```bash
python -m pip install -r requirements.txt
```

## 3) Virtual environment activation fails
- Linux/macOS:
```bash
source .venv/bin/activate
```
- Windows PowerShell:
```powershell
.venv\Scripts\activate
```
If PowerShell blocks scripts:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then activate again.

## 4) Port already in use (`8000` or `3000`)
Use different ports:
- Backend:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
```
- Frontend:
```bash
npm run dev -- -p 3001
```

## 5) `ModuleNotFoundError` in backend
Inside backend folder, with venv active:
```bash
python -m pip install -r requirements.txt
```

## 6) `npm install` fails
Try:
```bash
npm cache clean --force
npm install --legacy-peer-deps
```

## 7) Still stuck?
Use Docker option:
```bash
cd /tmp/workspace/ibrahimkhalilmasud/visionguard-ai/docker
docker compose up --build
```

---

## Project Folders (Quick Map)
- `backend/` → API server
- `frontend/` → Dashboard UI
- `docker/` → Docker setup
- `docs/` → Extra guides

Extra docs:
- `/docs/installation-guide.md`
- `/docs/beginner-setup-guide.md`
- `/docs/troubleshooting-guide.md`
- `/docs/gpu-setup-guide.md`
- `/docs/camera-setup-guide.md`
- `/docs/api-documentation.md`
