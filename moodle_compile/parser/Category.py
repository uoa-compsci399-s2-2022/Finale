class Category:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def __init__(self, name):
        self.name = name
        self.questions = []

    def addQuestion(self, newQuestion):
        self.questions.append(newQuestion)

    def convertQuestions(self, env):
        questionTemplate = []

        for questionOBJ in self.questions:
            template = env.get_template(questionOBJ.template)

            questionTemplate.append(template.render(question=questionOBJ))

            print(questionOBJ)

        self.questions = questionTemplate

