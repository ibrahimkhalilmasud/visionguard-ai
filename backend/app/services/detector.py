from dataclasses import dataclass


@dataclass
class DetectionResult:
    threat_type: str
    confidence: float


class ThreatDetector:
    supported_threats = [
        "human",
        "intrusion",
        "weapon",
        "fire",
        "smoke",
        "suspicious_activity",
        "face_recognition",
        "crowd",
        "abandoned_object",
    ]

    def infer(self) -> list[DetectionResult]:
        return []
