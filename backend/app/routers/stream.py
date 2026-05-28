from datetime import datetime

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter(tags=["stream"])


@router.websocket("/ws/telemetry")
async def telemetry_ws(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            await websocket.send_json({"timestamp": datetime.utcnow().isoformat(), "status": "running"})
            await websocket.receive_text()
    except WebSocketDisconnect:
        return
