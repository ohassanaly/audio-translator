Audio translator webapp built using [Pipecat](https://github.com/pipecat-ai/pipecat) </br> 
Monitoring was implemented using [OpenTelemetry](https://docs.pipecat.ai/server/utilities/opentelemetry#http-otlp-exporter-for-langfuse-etc) </br>
using the [Langfuse example](https://github.com/pipecat-ai/pipecat-examples/tree/main/open-telemetry/langfuse)</br>

Basic pipeline includes : </br>

1. **Audio Capture**: Your browser captures microphone audio and sends it via WebRTC
2. **Voice Activity Detection**: Silero VAD detects when you start and stop speaking
3. **Speech Recognition**: Deepgram converts your speech to text in real-time
4. **Language Processing**: OpenAI's GPT model generates an intelligent response
5. **Speech Synthesis**: Cartesia converts the response text back to natural speech
6. **Audio Playback**: The generated audio streams back to your browser