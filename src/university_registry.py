"""
University registry helpers.
Author: Sunil Paudel

Stores known institution -> website URLs for enrichment routing.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


BASE_DIR = Path(__file__).resolve().parent.parent
REGISTRY_PATH = BASE_DIR / "data" / "university_registry.json"


def load_registry(path: Path = REGISTRY_PATH) -> Dict[str, Any]:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("{}", encoding="utf-8")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            out: Dict[str, Any] = {}
            for k, v in data.items():
                if isinstance(v, str):
                    out[str(k)] = v
                elif isinstance(v, dict):
                    out[str(k)] = {
                        str(kk): str(vv)
                        for kk, vv in v.items()
                        if isinstance(vv, str)
                    }
            return out
    except Exception:
        pass
    return {}


def save_registry(registry: Dict[str, Any], path: Path = REGISTRY_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(registry, indent=2, ensure_ascii=False), encoding="utf-8")
