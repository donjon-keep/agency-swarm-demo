# Agency Swarm demo — two-agent company with real function tools

Proof-of-work repo for the AI Agent Developer application at
[agents.vrsen.ai](https://agents.vrsen.ai/jobs/). Built with
[Agency Swarm](https://github.com/VRSEN/agency-swarm) — the applicant's
framework of study — running against an OpenAI-compatible endpoint.

## What it is

- **Coordinator** agent: receives a business request, delegates once.
- **Analyst** agent: executes with two function tools —
  `SalesSnapshot` (mock CRM read) and `WriteNote` (mock note write).
- **Deterministic mock DB** — the demo is honest about data: the tools are
  mocked, the orchestration is real.

## Run the offline selftest (no API key needed)

```bash
pip install agency-swarm
python selftest.py
```

## Verified result (2026-11-09)

Live two-hop run captured in `live_run_output.txt`: Coordinator delegated
through its `send_message` tool to the Analyst, which called the
`SalesSnapshot` function tool and returned the Q2 summary — all against a
LOCAL OpenAI-compatible endpoint (no cloud API, no spend).

## Run a live turn (any OpenAI-compatible backend)

```bash
export OPENAI_API_KEY=your-key            # or the value your server expects
export OPENAI_BASE_URL=http://127.0.0.1:8080/v1   # local llama.cpp-class server
python agency.py
```

## Why this repo exists

Shows the working pieces an AI-agent developer owns end-to-end: agent
composition, function-tool wiring, delegation policies, and an offline
selftest so structure is verifiable before any API spend.
