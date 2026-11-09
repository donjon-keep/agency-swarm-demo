"""Function tools the demo agents expose. Deterministic, no network."""
import json

from agency_swarm.tools import BaseTool
from pydantic import Field


def _load():
    return json.load(open("data/mock_db.json", encoding="utf-8"))


from agency_swarm.tools import BaseTool


class SalesSnapshot(BaseTool):
    """Return the sales snapshot for a quarter (mock CRM read-only call)."""

    quarter: str = Field(..., description="Quarter key, e.g. Q1, Q2, Q3, Q4")

    def run(self, **kwargs) -> str:
        db = _load()
        snap = db.get(self.quarter)
        if not snap:
            return f"No snapshot for {self.quarter}. Available: {', '.join(db)}"
        return json.dumps(snap)


class WriteNote(BaseTool):
    """Append an analyst note to notes.log (mock note-keeping write call)."""

    note: str = Field(..., description="Short note text to log")

    def run(self, **kwargs) -> str:
        with open("data/notes.log", "a", encoding="utf-8") as fh:
            fh.write(self.note.replace("\n", " ") + "\n")
        return "note recorded"


