
from livekit.agents import Agent, AgentServer, AgentSession,JobContext, cli
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

server = AgentServer()
@server.rtc_session()
async def entrypoint(ctx: JobContext):
    session = AgentSession()

    await session.start(
        agent=TikiriliaAssistant(),
        room=ctx.room,
    )

    await ctx.connect()

if __name__ == "__main__":
    cli.run_app(server)

if __name__ == "__main__":
    cli.run_app(server)