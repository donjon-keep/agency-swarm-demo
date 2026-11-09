"""
Agency Swarm demo — a two-agent company with real function tools.

Runs against ANY OpenAI-compatible endpoint via env vars:
  OPENAI_API_KEY   -> your key (or the literal value your server expects)
  OPENAI_BASE_URL  -> e.g. a local llama.cpp / Strata server at http://127.0.0.1:8080/v1

Default (no env): dry-run selftest mode (structure + tool-schema validation, no API).

Layout:
  agents/coordinator.py     Coordinator agent (assigns work)
  agents/analyst.py         Data Analyst agent (does the work)
  tools/mock_tools.py       Function tools both agents can call
  agency.py                 Wires the three-block Agency together
  selftest.py               Offline selftest (no API key needed)
"""
from agency_swarm import Agency
from team.coordinator import Coordinator
from team.analyst import Analyst


def create_agency():
    coordinator = Coordinator()
    analyst = Analyst()
    return Agency(
        coordinator,
        analyst,
        communication_flows=[(coordinator, analyst)],  # Coordinator -> Analyst
    )


if __name__ == "__main__":
    agency = create_agency()
    # End-to-end: coordinator delegates to the analyst, analyst calls a tool.
    response = agency.get_response_sync(
        "Delegate to the Analyst: use the SalesSnapshot tool for Q2 and summarize the top line.",
    )
    print(response.final_output)
