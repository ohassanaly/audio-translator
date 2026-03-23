from pipecat.frames.frames import TTSSpeakFrame

from .services import create_llm, create_stt, create_tts
from .tools import build_context_aggregators, fetch_weather_from_api


def build_agent():
    stt = create_stt()
    tts = create_tts()
    llm = create_llm()

    # Register function tools used by the demo.
    llm.register_function("get_current_weather", fetch_weather_from_api)

    @llm.event_handler("on_function_calls_started")
    async def on_function_calls_started(service, function_calls):
        # Give the user audible acknowledgement while the function runs.
        await tts.queue_frame(TTSSpeakFrame("Let me check on that."))

    user_aggregator, assistant_aggregator = build_context_aggregators()
    return stt, llm, tts, user_aggregator, assistant_aggregator

