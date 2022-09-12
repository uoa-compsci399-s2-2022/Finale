class Question:
    def __init__(self, title, prompt, grade, answer, testcases, category):
        self.title = title
        self.prompt = prompt
        self.grade = grade
        self.answer = answer
        self.testcases = testcases
        self.category = category

    def __init__(self):
        self.title = "null"
        self.prompt = "null"
        self.answer = "null"
        self.testcases = []

    def setTitle(self, title):
        self.title = title

    def setPrompt(self, prompt):
        self.prompt = prompt

    def setGrade(self, grade):
        self.grade = grade

    def setAnswer(self, answer):
        self.answer = answer

    def setTestcases(self, testcases):
        self.testcases = testcases

    def setCategory(self, category):
        self.category = category

class TestCase:
    def __init__(self, example, display, testcode, stdin, expected):
        self.example = example
        self.display = display
        self.testcode = testcode
        self.stdin = stdin
        self.expected = expected

    def __init__(self):
        self.example = None
        self.display = None
        self.testcode = ""
        self.stdin = ""
        self.expected = ""

    def setexample(self, example):
        self.example = example

    def setdisplay(self, display):
        self.display = display

    def settestcode(self, testcode):
        self.testcode = testcode

    def addtestcode(self, testcode):
        if testcode == "":
            self.testcode += testcode
        else:
            self.testcode += "\n" + testcode

    def setstdin(self, stdin):
        self.stdin = stdin

    def addstdin(self, stdin):
        if stdin == "":
            self.stdin += stdin
        else:
            self.stdin += "\n" + stdin

    def setexpected(self, expected):
        self.expected = expected

    def addexpected(self, expected):
        if expected == "":
            self.expected += expected
        else:
            self.expected += "\n" + expected



