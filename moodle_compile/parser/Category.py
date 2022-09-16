class Category:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def __init__(self, name):
        self.name = name
        self.questions = []

    def addQuestion(self, newQuestion):
        self.questions.append(newQuestion)

    def convertQuestions(self, template):
        questionTemplate = []

        for questionOBJ in self.questions:
            questionTemplate.append(template.render(question=questionOBJ))

        self.questions = questionTemplate

