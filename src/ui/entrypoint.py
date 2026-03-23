from dotenv import load_dotenv
from pipecat.runner.types import RunnerArguments
from pipecat.runner.utils import create_transport

from backend.tracing import setup_tracing_if_enabled
from ui.runner import run_transport
from ui.transport import transport_params


async def bot(runner_args: RunnerArguments):
    """Main bot entry point compatible with Pipecat Cloud."""

    load_dotenv(override=True)
    enable_tracing = setup_tracing_if_enabled()

    transport = await create_transport(runner_args, transport_params)
    await run_transport(transport, enable_tracing=enable_tracing)

