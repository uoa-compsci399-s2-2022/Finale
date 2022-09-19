import pathlib
from jinja2 import Environment, FileSystemLoader
import re



class Question:
    def __init__(self, title, prompt, grade):
        self.title = title
        self.prompt = prompt
        self.grade = grade

    def __init__(self):
        self.title = "null"
        self.prompt = "null"
        self.grade = 10

    def setTitle(self, title):
        self.title = title

    def setPrompt(self, prompt):
        self.prompt = prompt

    def setGrade(self, grade):
        self.grade = grade


class CodeRunner(Question):
    def __init__(self):
        self.template = 'coderunner.xml'
    def setAnswer(self, answer):
        self.answer = answer

    def setCases(self, testcases):
        self.testcases = testcases


class MultipleChoice(Question):
    def __init__(self):
        self.template = 'multiplechoice.xml'
    def setCases(self, answers):
        self.answers = answers
