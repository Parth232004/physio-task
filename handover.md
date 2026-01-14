# Handover Documentation

## Repository Overview
This repository contains a simple AI Assistant implementation with intent classification, context management, response orchestration, and mock tools. It's designed as a self-contained demo system.

## Project Structure
```
├── ai_assistant/          # Main package
│   ├── __init__.py       # Package init
│   ├── router.py         # Intent classification
│   ├── manager.py        # Context management
│   ├── engine.py         # Response orchestration
│   ├── registry.py       # Tool registry with mocks
│   ├── demo.py           # CLI demo script
│   └── README.md         # Component documentation
├── tests/                # Test suite
│   └── test_orchestrator_v3.py
├── requirements.txt      # Dependencies (Python >= 3.6)
├── VALUES.md            # Value reflections
├── learning_notes.md    # Development notes
└── handover.md          # This file
```

## Setup Instructions
1. Ensure Python 3.6+ is installed
2. Clone the repository
3. Run the demo: `cd ai_assistant && python demo.py`
4. Run tests: `python -m unittest tests/test_orchestrator_v3.py`

## Key Components
- **Router**: Classifies user input into Q&A, Task, or Analysis intents
- **Manager**: Maintains conversation context (last 10 turns)
- **Engine**: Orchestrates responses based on intent and context
- **Registry**: Provides mock tools (calculator, summarizer, planner)

## FAQ for Future Developers

### Q: How does intent classification work?
A: The router uses simple keyword matching to classify inputs. Extend `classify_intent()` in `router.py` for more sophisticated classification.

### Q: Can I add real tools?
A: Yes, replace mock functions in `registry.py` with actual implementations. Update the `call_tool` method accordingly.

### Q: How is context managed?
A: The `ContextManager` stores the last 10 conversation turns. Modify `max_turns` in `__init__` to change the limit.


### Q: How do I extend the system?
A: Add new intents in `router.py`, handlers in `engine.py`, and tools in `registry.py`. Update tests in `tests/test_orchestrator_v3.py`.

### Q: Are there any known limitations?
A: This is a rule-based system with mock tools. No real AI, learning, or external integrations. Responses are deterministic.

### Q: How to run in production?
A: This is a demo. For production, integrate with real NLP libraries, databases, and APIs. Add error handling and logging.

## Maintenance Notes
- Keep mock tools clearly marked as simulations
- Update tests when adding features
- Maintain the self-contained nature (no external dependencies)
- Document any changes in this handover file