import pathlib
import base64
from .parser.Question import CodeRunner
from .parser.Question import MultipleChoice
from .parser.TestCase import TestCase
from .parser.Answer import Answer
from .parser.File import File
from .parser.Category import Category
from jinja2 import Environment, FileSystemLoader
import re

def getQuestion(dir):
    if dir.suffix == ".cr":
        newQuestion = CodeRunner()
    elif dir.suffix == ".mc":
        newQuestion = MultipleChoice()
    for p in dir.iterdir():
        if p.is_file():
            with open(p) as f:
                if p.suffix == ".py":
                    answer = f.read()
                    newQuestion.setAnswer(answer)

                elif p.suffix == ".md":
                    prompt = f.read()
                    newQuestion.setPrompt(prompt)


                elif p.suffix == ".toml":
                    cases = []
                    lines = iter(f.readlines())
                    for line in lines:
                        if line.strip() == "":
                            continue
                        if "[[testcases]]" in line:
                            cases.append(TestCase())
                        elif "[[answers]]" in line:
                            cases.append(Answer())
                        else:
                            splitLine = line.split("=")
                            #take what's before an equal sign and that's our variable name we are manipulating
                            attributeName = splitLine[0].strip()
                            attributeValue = None
                            #get everything inbetween the three ''' '''
                            if "'''" not in line:
                                attributeValue = splitLine[1].strip()
                            else:
                                equator = splitLine[1].split("'''")
                                attributeValue = equator[1]
                                if len(equator) == 2:
                                    while True:
                                        nextLine = next(lines)
                                        if "'''" in nextLine:
                                            attributeValue += nextLine.split("'''")[0]
                                            break
                                        attributeValue += nextLine
                            cases[-1].__setattr__(attributeName, attributeValue)
                    newQuestion.setCases(cases)
        else:
            for sf in p.iterdir():
                print(sf)
                if sf.is_file():
                    with open(sf) as f:
                        content = f.read()
                        newFile = File(sf.name, '/')
                        newFile.setContent(base64.b64encode(bytes(content, "utf-8")))
                        newQuestion.addFile(newFile)
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
    file_loader = FileSystemLoader('moodle_compile/templates')
    env = Environment(loader=file_loader)

    #get our questions/answers
    categories = getCategories(root)

    quizTemplate = env.get_template('quiz.xml')

    for cat in categories:
        cat.convertQuestions(env)

    output = quizTemplate.render(categories=categories)


    return output