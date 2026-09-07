"""
Utility: clear `target_board_id` from persisted research_state.json files under backend/data/workspaces.
Run this locally if you want to remove historical suggestions from workspace data.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1] / "data" / "workspaces"
count = 0
for ws in ROOT.glob("*/.hardcoreai/research_state.json"):
    try:
        data = json.loads(ws.read_text(encoding="utf-8"))
    except Exception:
        continue
    if data.get("target_board_id") is not None:
        data["target_board_id"] = None
        ws.write_text(json.dumps(data, indent=2), encoding="utf-8")
        count += 1
print(f"Cleared target_board_id in {count} research_state files.")
