# AI Assistant

A simple, deterministic AI assistant that classifies user intents and generates responses using mock tools. No autonomy, no learning memory, no system internals exposed.

## Architecture

```
User Input
    ↓
classify_intent() → Q&A / Task request / Analysis request
    ↓
Context Manager (last 10 turns)
    ↓
Handler (qa_handler / task_handler / analysis_handler)
    ↓
Tool Registry (calculator, summarizer, planner)
    ↓
Response
```

## Components

- `router.py`: Intent classifier (deterministic keyword-based)
- `manager.py`: Context manager (conversation history, max 10 turns)
- `engine.py`: Response orchestration engine
- `registry.py`: Tool registry with mock tools (calculator, summarizer, planner)
- `demo.py`: CLI demo with decision logging

## Running the Demo

```bash
cd ai_assistant
python demo.py
```

## Intent Types

| Intent | Keywords | Handler |
|--------|----------|---------|
| Q&A | what, how, why, when, where, who, is, are, does, ? | handle_qa() |
| Task request | calculate, compute, do, execute, run, perform | handle_task() |
| Analysis request | analyze, summarize, review, examine | handle_analysis() |

## Decision Logging

The demo shows clear decision logging:
- `[DECISION] Intent classified: <type>`
- `[DECISION] Routing path: input -> classify_intent() -> <type>_handler -> response`
