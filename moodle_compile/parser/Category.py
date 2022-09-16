class Category:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def __init__(self, name):
        self.name = name
        self.questions = []

    def addQuestion(self, newQuestion):
        self.questions.append(newQuestion)