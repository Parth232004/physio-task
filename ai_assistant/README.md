# AI Assistant

This is a simple AI assistant that classifies user intents into Q&A, Task request, or Analysis request, maintains short-term context, and generates responses using mock tools.

## Components

- `router.py`: Intent classifier
- `manager.py`: Context manager
- `engine.py`: Response engine
- `registry.py`: Tool registry with mock tools
- `demo.py`: CLI demo script

## Running the Demo

Run `cd ai_assistant && python demo.py` to start the CLI assistant.