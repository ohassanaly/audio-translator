from loguru import logger
from pipecat.frames.frames import LLMRunFrame
from pipecat.pipeline.runner import PipelineRunner
from pipecat.pipeline.task import PipelineParams, PipelineTask

from backend.agent import build_agent
from backend.pipeline import build_pipeline


async def run_transport(transport, *, enable_tracing: bool):
    logger.info("Starting bot")

    stt, llm, tts, user_aggregator, assistant_aggregator = build_agent()
    pipeline = build_pipeline(
        transport=transport,
        stt=stt,
        llm=llm,
        tts=tts,
        user_aggregator=user_aggregator,
        assistant_aggregator=assistant_aggregator,
    )

    task = PipelineTask(
        pipeline,
        params=PipelineParams(
            enable_metrics=True,
            enable_usage_metrics=True,
        ),
        enable_tracing=enable_tracing,
    )

    @transport.event_handler("on_client_connected")
    async def on_client_connected(transport, client):
        logger.info("Client connected")
        # Kick off the conversation.
        await task.queue_frames([LLMRunFrame()])

    @transport.event_handler("on_client_disconnected")
    async def on_client_disconnected(transport, client):
        logger.info("Client disconnected")
        await task.cancel()

    runner = PipelineRunner(handle_sigint=False)
    await runner.run(task)

