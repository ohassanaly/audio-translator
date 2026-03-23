import os

from loguru import logger
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from pipecat.utils.tracing.setup import setup_tracing


def tracing_enabled_from_env() -> bool:
    return bool(os.getenv("ENABLE_TRACING"))


def setup_tracing_if_enabled() -> bool:
    """Enable OpenTelemetry tracing when `ENABLE_TRACING` is set."""

    enabled = tracing_enabled_from_env()
    if not enabled:
        return False

    # Create the exporter
    otlp_exporter = OTLPSpanExporter()

    # Set up tracing with the exporter
    setup_tracing(
        service_name="pipecat-demo",
        exporter=otlp_exporter,
        console_export=bool(os.getenv("OTEL_CONSOLE_EXPORT")),
    )
    logger.info("OpenTelemetry tracing initialized")
    return True

