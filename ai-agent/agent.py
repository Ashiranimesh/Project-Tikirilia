from google.genai import types
from dotenv import load_dotenv
from livekit.agents import Agent, AgentServer, AgentSession, JobContext, cli
from livekit.plugins import google

load_dotenv()


class TikiriliaAssistant(Agent):
    def __init__(self):
        super().__init__(
            instructions="""
            You are Tikirilia, a friendly and cheerful AI companion
representing Sri Lanka.

Your personality:
- Warm, welcoming, and naturally conversational.
- Speak like a friendly Sri Lankan companion.
- Be enthusiastic when sharing interesting things.

Language behaviour:
- If the user speaks English, respond in English.
- If the user speaks Sinhala, respond in Sinhala.
- If the user mixes Sinhala and English, respond naturally
  using the same language style.
- Never translate everything automatically.
- Use natural, conversational language.

Your responsibilities:
- Introduce Sri Lankan tourist destinations.
- Share interesting facts about Sri Lankan culture.
- Explain local traditions, food, and festivals.
- Help users discover beautiful places in Sri Lanka.

Keep responses clear, friendly, and not unnecessarily long.
            """,
            llm=google.realtime.RealtimeModel(
                 model="gemini-3.8-live",
                 voice="Sulafat",
                 temperature=0.8,
                 input_audio_transcription=types.AudioTranscriptionConfig(),
          ),
            
        )

server = AgentServer()

@server.rtc_session()
async def entrypoint(ctx: JobContext):
    session = AgentSession(
        user_away_timeout=20.0
    )

    # Detect user inactivity
    @session.on("user_state_changed")
    def on_user_state_changed(event):
        if event.new_state == "away":
            print("User is inactive. Closing conversation...")
            session.shutdown()

    # Detect goodbye phrase
    @session.on("user_input_transcribed")
    def on_user_input_transcribed(event):
        if event.is_final:
            transcript = event.transcript.lower()

            print(f"Recognized speech: {event.transcript!r}")

            # Remove punctuation
            transcript = transcript.replace(",", "").replace(".", "")
            transcript = transcript.replace("!", "").replace("?", "")

            # Supported goodbye phrases
            goodbye_phrases = [
                "goodbye tikirilia",
                "goodbye",
                "bye tikirilia",
                "see you tikirilia"
            ]

            if transcript.strip() in goodbye_phrases:
                print(f"Goodbye phrase detected: {transcript}")
                print("Closing conversation...")
                session.shutdown()

    # Start the AI agent
    await session.start(
        agent=TikiriliaAssistant(),
        room=ctx.room,
    )

    await ctx.connect()


if __name__ == "__main__":
    cli.run_app(server)

