from pathlib import Path


class RecordingService:
    def __init__(self, base_dir: str = "recordings"):
        self.base_path = Path(base_dir)
        self.base_path.mkdir(parents=True, exist_ok=True)

    def list_recordings(self) -> list[str]:
        return [f.name for f in self.base_path.glob("*.mp4")]
