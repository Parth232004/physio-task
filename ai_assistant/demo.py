#!/usr/bin/env python3

from engine import ResponseEngine

def main():
    engine = ResponseEngine()
    print("AI Assistant Demo")
    print("Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        # Log intent
        from router import classify_intent
        intent = classify_intent(user_input)
        print(f"[LOG] Intent classified as: {intent}")

        # Generate response
        response = engine.generate_response(user_input)
        print(f"[LOG] Response generated via {intent} handler")
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()