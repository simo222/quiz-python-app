import unittest
from unittest.mock import patch, mock_open
import io
import sys
import importlib.util
import os
import json

spec = importlib.util.spec_from_file_location("quiz_module", os.path.join(os.path.dirname(__file__), "1-question-quiz-no-lambda-functions.py"))
quiz_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(quiz_module)

class TestQuiz(unittest.TestCase):
    @patch('builtins.input', side_effect=['A'])
    def test_multiple_choice_question_correct(self, mock_input):
        # Redirect stdout to capture print statements
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Prepare a single multiple choice question with labeled choices
        questions = {
            "question1": {
                "question": "What is the name of the Kubernetes API object that represents a group of containers?",
                "choices": {
                    "A": "Pod",
                    "B": "Service",
                    "C": "Deployment",
                    "D": "ReplicaSet"
                },
                "answer": "A"
            }
        }

        # Patch open to simulate reading questions.json
        m = mock_open(read_data=json.dumps(questions))
        with patch('builtins.open', m):
            quiz_module.quiz()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Correct", output)
        self.assertIn("Your final score is: 1/1", output)

    @patch('builtins.input', side_effect=['A,C'])
    def test_multiple_correct_answers(self, mock_input):
        # Redirect stdout to capture print statements
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Prepare a multiple answer question
        questions = {
            "question1": {
                "question": "Which commands can be used to manage Kubernetes resources? (Select all that apply)",
                "choices": {
                    "A": "kubectl apply",
                    "B": "kubectl get",
                    "C": "kubectl logs",
                    "D": "kubectl config"
                },
                "answer": ["A", "C"]
            }
        }

        # Patch open to simulate reading questions.json
        m = mock_open(read_data=json.dumps(questions))
        with patch('builtins.open', m):
            quiz_module.quiz()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Correct", output)
        self.assertIn("Your final score is: 1/1", output)

if __name__ == '__main__':
    unittest.main()
