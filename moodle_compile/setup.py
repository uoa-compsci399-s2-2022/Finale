import pathlib
from .parser.Question import Question
from .parser.TestCase import TestCase
from .parser.Answer import Answer
from .parser.Category import Category
from jinja2 import Environment, FileSystemLoader
import re

def getQuestion(dir):
    newQuestion = Question()
    for p in dir.iterdir():
        with open(p) as f:

            if p.suffix == ".py":
                answer = f.read()
                newQuestion.setAnswer(answer)

            elif p.suffix == ".md":
                prompt = f.read()
                newQuestion.setPrompt(prompt)


            elif p.suffix == ".toml":
                newCase = None
                lines = iter(f.readlines())
                for line in lines:
                    if line.strip() == "":
                        continue
                    if "[[testcases]]" in line:
                        newCase = TestCase()
                    elif "[[answers]]" in line:
                        newCase = Answer()
                    else:
                        splitLine = line.split("=")
                        #take what's before an equal sign and that's our variable name we are manipulating
                        attributeName = splitLine[0].strip()
                        attributeValue = None
                        #get everything inbetween the three ''' '''
                        if "'''" not in line:
                            variableValue = splitLine[1].strip()
                        else:
                            equator = splitLine[1].split("'''")
                            variableValue = equator[1]
                            if len(equator) == 2:
                                while True:
                                    nextLine = next(lines)
                                    if "'''" in nextLine:
                                        variableValue += nextLine.split("'''")[0]
                                        break
                                    variableValue += nextLine
                        newCase.__setattr__(attributeName, attributeValue)





            #newQuestion.setTestcases(testcases)
    return newQuestion

def getCategories(dir, cat = []):
    for p in dir.iterdir():
        if p.is_file():
            parentFolder = p.parent
            #get folder name(name of question)
            [questionName, type] = parentFolder.name.split(".")
            question = getQuestion(dir)
            question.setTitle(questionName)

            cat[-1].addQuestion(question)
            return cat
        if p.name.__str__()[-3] != ".":
            catName = str(pathlib.Path(*p.parts[1:]))
            newCat = Category(catName)
            cat.append(newCat)
        newCat = getCategories(p, cat)
    return cat


def Quiz(root):
    #setup templates location
    file_loader = FileSystemLoader('moodle_compile/templates')
    env = Environment(loader=file_loader)
    #get our questions/answers
    categories = getCategories(root)
    quizTemplate = env.get_template('quiz.xml')
    coderunnerTemplate = env.get_template('coderunner.xml')

    for cat in categories:
        cat.convertQuestions(coderunnerTemplate)

    output = quizTemplate.render(categories=categories)


    return output