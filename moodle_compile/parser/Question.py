import pathlib
from jinja2 import Environment, FileSystemLoader
import re



class Question:
    def __init__(self, title, prompt, grade):
        self.title = title
        self.prompt = prompt
        self.grade = grade
        self.files = []
        

    def __init__(self):
        self.title = "null"
        self.prompt = "null"
        self.grade = 10
        self.files = []

    def setTitle(self, title):
        self.title = title

    def setPrompt(self, prompt):
        self.prompt = prompt

    def setGrade(self, grade):
        self.grade = grade
    
    def addFile(self, file):
        self.files.append(file)


class CodeRunner(Question):
    def __init__(self):
        super(CodeRunner, self).__init__()
        self.template = 'coderunner.xml'

    def setAnswer(self, answer):
        self.answer = answer

    def setCases(self, testcases):
        self.testcases = testcases

    def testTestCases(self):
        #move the input part to a previous line
        #convert Answer inputs to console
        #testCaseCode = self.answer.replace('input(', 'print(')
        #print(testCaseCode)
        for loopNum, test in enumerate(self.testcases):
            test.testExpected(self, loopNum)


class MultipleChoice(Question):
    def __init__(self):
        super(MultipleChoice, self).__init__()
        self.template = 'multiplechoice.xml'
    def setCases(self, answers):
        self.answers = answers

class ShortAnswer(Question):
    def __init__(self):
        super(ShortAnswer, self).__init__()
        self.template = 'shortanswer.xml'
    def setCases(self, answers):
        self.answers = answers

    def setFeedback(self, feedback):
        self.feedback = feedback
