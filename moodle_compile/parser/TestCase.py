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




