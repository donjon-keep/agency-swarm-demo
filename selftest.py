"""Offline selftest: validates structure and tool wiring without an API key."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from team.analyst import Analyst  # noqa: E402
from team.coordinator import Coordinator  # noqa: E402
from agency import create_agency  # noqa: E402
from capabilities.mock_tools import SalesSnapshot, WriteNote  # noqa: E402

checks = []


def check(name, fn):
    try:
        result = fn()
        checks.append((name, "PASS", result))
    except Exception as exc:  # pragma: no cover
        checks.append((name, "FAIL", f"{type(exc).__name__}: {exc}"))


check("mock_db has 4 quarters", lambda: (
    lambda db: f"{len(db)} quarters" if len(db) == 4 else 1 / 0
)(json.load(open("data/mock_db.json", encoding="utf-8"))))
check("SalesSnapshot returns Q2", lambda: (lambda out: out if "58750" in out else 1 / 0)(SalesSnapshot(quarter="Q2").run()))
check("SalesSnapshot unknown quarter handled", lambda: (lambda out: out if "No snapshot for Q9" in out else 1 / 0)(SalesSnapshot(quarter="Q9").run()))
check("WriteNote records", lambda: (lambda out: out if "recorded" in out else 1 / 0)(WriteNote(note="selftest marker").run()))
check("tools registered on Analyst", lambda: (
    lambda src: "SalesSnapshot + WriteNote wired"
    if "SalesSnapshot" in src and "WriteNote" in src else 1 / 0
)(open("team/analyst.py", encoding="utf-8").read()))
check("agency assembles", lambda: (lambda a: "full agency graph built" if a else 1 / 0)(__import__("agency").create_agency()))

print("AGENCY-SWARM DEMO SELFTEST")
all_pass = True
for name, status, info in checks:
    print(f"  [{status}] {name}" + (f" -> {info}" if info else ""))
    all_pass = all_pass and status == "PASS"
print("SELFTEST:", "ALL PASS" if all_pass else "FAILURES PRESENT")
sys.exit(0 if all_pass else 1)
