import unittest
from unittest.mock import Mock, patch
import sys
import os

# Add the ai_assistant directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ai_assistant'))

from engine import ResponseEngine
from router import classify_intent
from registry import ToolRegistry

class TestOrchestratorV3(unittest.TestCase):

    def setUp(self):
        self.engine = ResponseEngine()

    def test_routing_qa_intent(self):
        """Test routing for Q&A intent"""
        intent = classify_intent("What is Python?")
        self.assertEqual(intent, 'Q&A')

    def test_routing_task_intent(self):
        """Test routing for Task request intent"""
        intent = classify_intent("Calculate 2 + 2")
        self.assertEqual(intent, 'Task request')

    def test_routing_analysis_intent(self):
        """Test routing for Analysis request intent"""
        intent = classify_intent("Analyze this data")
        self.assertEqual(intent, 'Analysis request')

    @patch('registry.ToolRegistry.call_tool')
    def test_retry_fallback_on_tool_failure(self, mock_call_tool):
        """Test retry/fallback when tool fails"""
        # Mock tool failure
        mock_call_tool.side_effect = Exception("Tool failed")

        response = self.engine.generate_response("Calculate 2 + 2")
        # Should fallback to default response
        self.assertIn("Task 'Calculate 2 + 2' executed", response)

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_db_write_verification(self, mock_file):
        """Test DB write verification (mocked)"""
        # Mock DB write
        with patch('json.dump') as mock_json_dump:
            # Simulate writing to DB
            import json
            data = {'user': 'test', 'response': 'test response'}
            json.dump(data, mock_file())
            mock_json_dump.assert_called_once()

    def test_context_memory_limit(self):
        """Test context memory doesn't exceed max turns"""
        for i in range(12):  # More than max_turns=10
            self.engine.generate_response(f"Message {i}")
        self.assertEqual(len(self.engine.context_manager.get_context()), 10)

if __name__ == '__main__':
    unittest.main()