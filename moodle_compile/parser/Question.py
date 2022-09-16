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