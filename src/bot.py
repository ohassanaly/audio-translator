# Pipecat expects a top-level `bot` coroutine in this module.
# We keep this file as the entrypoint and move the implementation into `src/ui/` and `src/backend/`.
from ui.entrypoint import bot  # noqa: E402

if __name__ == "__main__":
    from pipecat.runner.run import main

    main()