from agency_swarm import Agent


class Analyst(Agent):
    """Executes delegated work with function tools."""

    def __init__(self):
        from capabilities.mock_tools import SalesSnapshot, WriteNote

        super().__init__(
            name="Analyst",
            description="Performs lookups and writes notes using its function tools.",
            instructions="./agents/instructions_analyst.md",
            tools=[SalesSnapshot, WriteNote],
        )
