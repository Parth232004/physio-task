class ContextManager:
    def __init__(self, max_turns=10):
        self.conversation_history = []
        self.max_turns = max_turns

    def add_turn(self, user_input, assistant_response):
        """
        Add a turn to the conversation history.
        """
        self.conversation_history.append({
            'user': user_input,
            'assistant': assistant_response
        })
        if len(self.conversation_history) > self.max_turns:
            self.conversation_history.pop(0)

    def get_context(self):
        """
        Get the current context as a list of recent turns.
        """
        return self.conversation_history.copy()