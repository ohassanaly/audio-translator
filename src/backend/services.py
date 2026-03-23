import os

from pipecat.services.cartesia.tts import CartesiaTTSService
from pipecat.services.deepgram.stt import DeepgramSTTService
from pipecat.services.openai.llm import OpenAILLMService


def create_stt() -> DeepgramSTTService:
    return DeepgramSTTService(api_key=os.getenv("DEEPGRAM_API_KEY"))


def create_tts() -> CartesiaTTSService:
    return CartesiaTTSService(
        api_key=os.getenv("CARTESIA_API_KEY"),
        settings=CartesiaTTSService.Settings(
            voice="71a7ad14-091c-4e8e-a314-022ece01c121",  # British Reading Lady
        ),
    )


def create_llm() -> OpenAILLMService:
    return OpenAILLMService(
        api_key=os.getenv("OPENAI_API_KEY"),
        settings=OpenAILLMService.Settings(
            temperature=0.5,
            system_instruction=(
                "You are a helpful LLM in a WebRTC call. Your goal is to demonstrate your capabilities "
                "in a succinct way. Your output will be converted to audio so don't include special "
                "characters in your answers. Respond to what the user said in a creative and helpful way."
            ),
        ),
    )

