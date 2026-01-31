#!/usr/bin/env python3
"""
CLI Demo for the AI Assistant.
Demonstrates deterministic intent routing with clear decision logging.
"""

from engine import ResponseEngine
from router import classify_intent


def main():
    engine = ResponseEngine()
    print("=" * 50)
    print("AI Assistant Demo")
    print("Deterministic Intent Router + Tool Simulation")
    print("=" * 50)
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("\nGoodbye!")
            break

        # Step 1: Classify intent
        intent = classify_intent(user_input)
        print(f"[DECISION] Intent classified: {intent}")

        # Step 2: Generate response with full routing path
        response = engine.generate_response(user_input)

        # Step 3: Show routing path used
        print(f"[DECISION] Routing path: input -> classify_intent() -> {intent.replace(' ', '_')}_handler -> response")
        print(f"Assistant: {response}")
        print()


if __name__ == "__main__":
    main()
