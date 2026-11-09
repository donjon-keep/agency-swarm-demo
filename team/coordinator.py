from agency_swarm import Agent


class Coordinator(Agent):
    """Routes tasks to the right worker and keeps a running status."""

    def __init__(self):
        super().__init__(
            name="Coordinator",
            description="Receives business requests, breaks them down, delegates to the Analyst.",
            instructions="./agents/instructions_coordinator.md",
            tools=[],
        )
