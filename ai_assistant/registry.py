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
        # Mock summary
        return f"Summary of '{text}': This is a summarized version."

    def mock_planner(self, task):
        # Mock planning
        return f"Plan for '{task}': Step 1, Step 2, Done."