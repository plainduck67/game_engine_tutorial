# scenes.py
import json
import pathlib
from typing import Dict, Any

DATA_DIR = pathlib.Path(__file__).parent / "data"

class SceneRepository:
    """Loads scene JSON on demand and caches it."""
    def __init__(self):
        self._cache: Dict[str, Dict[str, Any]] = {}

    def get_turn(self, scene: str, turn: str) -> Dict[str, Any]:
        if scene not in self._cache:
            file_path = DATA_DIR / f"{scene}.json"
            print(f"[DEBUG] loading {file_path.name}")
            with open(file_path, encoding="utf-8") as f:
                self._cache[scene] = json.load(f)["turns"]
        return self._cache[scene][turn]
