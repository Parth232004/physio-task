from router import classify_intent
from manager import ContextManager
from registry import ToolRegistry

class ResponseEngine:
    def __init__(self):
        self.context_manager = ContextManager()
        self.tool_registry = ToolRegistry()

    def generate_response(self, user_input):
        """
        Generate a response based on user input, intent, and context.
        """
        intent = classify_intent(user_input)
        context = self.context_manager.get_context()

        if intent == 'Q&A':
            response = self.handle_qa(user_input, context)
        elif intent == 'Task request':
            response = self.handle_task(user_input, context)
        elif intent == 'Analysis request':
            response = self.handle_analysis(user_input, context)
        else:
            response = "I'm sorry, I didn't understand that."

        # Add to context
        self.context_manager.add_turn(user_input, response)

        return response

    def handle_qa(self, user_input, context):
        # Simple Q&A response
        return f"Regarding your question '{user_input}', here's a basic answer."

    def handle_task(self, user_input, context):
        # For task, try to use tools
        if 'calculate' in user_input.lower():
            result = self.tool_registry.call_tool('calculator', user_input)
            return f"Calculation result: {result}"
        return f"Task '{user_input}' executed."

    def handle_analysis(self, user_input, context):
        # Use summarizer
        result = self.tool_registry.call_tool('summarizer', user_input)
        return f"Analysis: {result}"