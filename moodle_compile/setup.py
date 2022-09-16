import pathlib
from .parser.Question import Question
from .parser.TestCase import TestCase
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

def getCategories(dir):
    cat = []
    question = None
    for p in dir.iterdir():
        if p.is_file():
            question = getQuestion(dir)
            question.setCategory(str(pathlib.Path(*p.parts[1:])))
            return cat, question
        cat.append(str(pathlib.Path(*p.parts[1:])))
        [newCat, question] = getCategories(p)
        question = question
        cat += newCat
    return cat, question


def Quiz(root):
    #setup templates location
    file_loader = FileSystemLoader('moodle_compile/templates')
    env = Environment(loader=file_loader)
    #get our questions/answers
    [categories, question] = getCategories(root)
    questions = [question]

    template = env.get_template('quiz.xml')
    output = template.render(categories=categories, questions=questions)

    return output