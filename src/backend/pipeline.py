from pipecat.pipeline.pipeline import Pipeline


def build_pipeline(transport, stt, llm, tts, user_aggregator, assistant_aggregator) -> Pipeline:
    return Pipeline(
        [
            transport.input(),
            stt,
            user_aggregator,
            llm,
            tts,
            transport.output(),
            assistant_aggregator,
        ]
    )

