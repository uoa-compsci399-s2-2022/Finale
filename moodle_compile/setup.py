import pathlib
from .parser.Question import Question
from .parser.TestCase import TestCase
from .parser.Category import Category
from jinja2 import Environment, FileSystemLoader
import re

def getQuestion(dir):
    newQuestion = Question()
    #print(dir)
    for p in dir.iterdir():
        with open(p) as f:
            if p.name == "answer.py":
                answer = f.read()
                newQuestion.setAnswer(answer)

            elif p.name == "prompt.md":
                prompt = f.read()
                newQuestion.setPrompt(prompt)
                newQuestion.setTitle(prompt[:15])


            elif p.name == "testcases.toml":
                #read all the test cases and create testcase
                testcases = []
                prev=None
                testcaseRead = f.readlines()
                for line in testcaseRead:
                    #check if continuation of testcode, stdin or expected

                    if prev is not None:
                        reset = False
                        line = line.replace("\n", "")
                        if "'''" in line:
                            line = line.replace("'''", "")
                            reset = True

                        if prev == "testcode":
                            testcases[len(testcases) - 1].addtestcode(line)
                        elif prev == "stdin":
                            testcases[len(testcases) - 1].addstdin(line)
                        elif prev == "expected":
                            testcases[len(testcases) - 1].addexpected(line)

                        if reset is True:
                            prev = None
                    #current testcase = len(testcases)
                    elif '[[testcases]]' in line:
                        testcases.append(TestCase())
                    elif "example" in line:
                        if "true" in line.lower():
                            testcases[len(testcases) - 1].setexample("1")
                        else:
                            testcases[len(testcases) - 1].setexample("0")
                    elif "display" in line:
                        testcases[len(testcases) - 1].setdisplay(re.findall(r'"([^"]*)"', line)[0])
                    elif "testcode" in line:
                        line = line.split("'''")
                        testcases[len(testcases) - 1].settestcode(line[1])
                        if len(line) != 3:
                            prev = "testcode"
                    elif "stdin" in line:
                        line = line.split("'''")
                        testcases[len(testcases) - 1].setstdin(line[1].replace("\n", ""))
                        if len(line) != 3:
                            prev = "stdin"
                    elif "expected" in line:
                        line = line.split("'''")
                        testcases[len(testcases) - 1].setexpected(line[1].replace("\n", ""))
                        if len(line) != 3:
                            prev = "expected"
                newQuestion.setTestcases(testcases)
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
    for cat in categories:
        print(cat.name, len(cat.questions))
    template = env.get_template('quiz.xml')
    output = template.render(categories=categories)

    return output