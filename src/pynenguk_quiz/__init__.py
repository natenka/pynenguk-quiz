from importlib import resources
import json


__version__ = "0.7.3"

ALL_QUESTIONS = json.loads(resources.read_text("pynenguk_quiz", "questions.json"))
