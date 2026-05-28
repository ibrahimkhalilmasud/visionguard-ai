from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import cv2


@dataclass
class CameraDiagnostics:
    reachable: bool
    fps: float | None
    message: str


class UniversalCameraManager:
    supported_protocols = {
        "usb",
        "laptop",
        "rtsp",
        "onvif",
        "xiaomi",
        "imou",
        "dahua",
        "hikvision",
        "ezviz",
        "reolink",
        "tapo",
        "dvr",
        "nvr",
        "ip",
    }

    def test_stream(self, source: str) -> CameraDiagnostics:
        cap = cv2.VideoCapture(source)
        if not cap.isOpened():
            return CameraDiagnostics(reachable=False, fps=None, message="Unable to open stream")
        fps = cap.get(cv2.CAP_PROP_FPS) or None
        cap.release()
        return CameraDiagnostics(reachable=True, fps=fps, message="Stream healthy")

    def health_status(self, last_seen: datetime | None) -> str:
        if not last_seen:
            return "unknown"
        delta = datetime.utcnow() - last_seen
        return "healthy" if delta.total_seconds() < 30 else "degraded"
