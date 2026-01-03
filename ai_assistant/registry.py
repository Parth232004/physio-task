class ToolRegistry:
    def __init__(self):
        self.tools = {
            'calculator': self.mock_calculator,
            'summarizer': self.mock_summarizer,
            'planner': self.mock_planner
        }

    def call_tool(self, tool_name, input_data):
        """
        Call a tool by name with input data.
        """
        if tool_name in self.tools:
            return self.tools[tool_name](input_data)
        else:
            return f"Tool '{tool_name}' not found."

    def mock_calculator(self, expression):
        # Simple mock: assume expression like "2 + 2"
        try:
            # Basic eval for demo
            result = eval(expression)
            return str(result)
        except:
            return "Invalid calculation."

    def mock_summarizer(self, text):
        # Basic mock summary: return first 50 characters or key phrases
        words = text.split()
        if len(words) > 10:
            summary = ' '.join(words[:10]) + '...'
        else:
            summary = text
        return f"Summary: {summary}"

    def mock_planner(self, task):
        # Basic mock planning: break into steps based on keywords
        steps = []
        if 'analyze' in task.lower():
            steps = ["Gather data", "Identify patterns", "Generate insights"]
        elif 'calculate' in task.lower():
            steps = ["Parse input", "Perform calculation", "Return result"]
        else:
            steps = ["Define objective", "Execute task", "Review outcome"]
        plan = f"Plan for '{task}':\n" + '\n'.join(f"- {step}" for step in steps)
        return plan