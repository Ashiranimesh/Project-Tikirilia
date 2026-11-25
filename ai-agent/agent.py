
from livekit.agents import Agent, AgentServer, AgentSession, cli
from livekit.plugins import google


class TikiriliaAssistant(Agent):
    def __init__(self):
        super().__init__(
            instructions="""
            You are Tikirilia, a friendly AI companion
            representing Sri Lanka.

            Your responsibilities:
            - Welcome users warmly.
            - Help users learn about Sri Lankan culture.
            - Introduce Sri Lankan tourist destinations.
            - Explain local traditions and festivals.
            - Communicate naturally and politely.

            Keep your responses friendly, clear, and conversational.
            """,
            llm=google.realtime.RealtimeModel(
                 voice="Puck",
                 temperature=0.8,
          ),
            
        )