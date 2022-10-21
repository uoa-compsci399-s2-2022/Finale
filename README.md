<!-- TITLE -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <a href="https://freeimage.host/i/QExVpf"><img src="https://iili.io/QExVpf.md.png" alt="QExVpf.md.png" border="0"></a>
  </a>

  <p align="center">
    Python program that can transform a suite of Moodle Question data 
    <br>
    in a format specified by the client to Moodle XML and back.
  </p>
</div>

<br>

<!-- ABOUT THE PROJECT -->
## About The Project
The process to write CodeRunner questions with Moodle is difficult and the number of options makes question creation long and tedious. This means that teaching staff spend large amounts of time working simply writing out the questions, and the process leads to a high incidence of question errors.

Based on <a href="https://github.com/James-Ansley/moodle-toml">Toodle</a> by <a href="https://github.com/James-Ansley">@James-Ansley</a>, `FiNoodle` by Finale supports various question types (including CodeRunner, short answer, multiple choice, etc.) and provide warnings for common errors in generating questions. FiNoodle also various supports question templates to generate questions in a consistent and precise format.

<br>

<!-- BUILT WITH -->
### Built With

* Python (3.10)
* Moodle
* XML
* Jinja (3.1.2)

<br>
<hr>
<br>

<!-- INSTALLATION -->
## Installation
```
pip install FiNoodle
```
FiNoodle supports installing using pip. Enter the command above in the project folder to install FiNoodle.

<br>
<hr>
<br>

<!-- USAGE -->
## Usage
install the package using `pip install FiNoodle`
place folder names `questions` in your root directory(where your main script is) and run `FiNoodle.exportQuestions.build()`. An output file called `out.xml` will be generated in the project folder which can be loaded to Moodle directly.

Or use included function named `FiNoodle.exportQuestions.createBlankQuestion(qpath, name, qtype)` to generate a new question. the question will be generated at `questions/"qpath"` and will be named whatever name is. qtype can be any of our supported Question types below.

To use our targeted export, or use a different questions folder directory, our included build command can take 2 attributes as seen below.
```py
    build(root: Path = Path("questions"), globPattern = {
        "exportGlob": "",
        "blackListGlob": "None",
        "IterateChildren": False
    }):
```

root, is the root of the questions you wish to export(leave blank for default location which is in your root directory)

The glob patterns allows targeted exporting and blacklisting of questions. IterateChildren will let you get all the children of a whitelisted directory if you wish to export a group of questions.

# File usages 

## prompt.md
This will be the question prompt, ask your question you want them to solve here

## Testcases.toml

writing testcases is simple, customizable options are as follows

```toml
[[testcases]]
example = true | false
display = '''SHOW''' | '''HIDE'''
testcode = '''''' | add testcode
stdin = '''12.5
5.5''' | none
expected ='''Enter the base of the rectangle in centimetres: 12.5
Enter the height of the rectangle in centimetres: 5.5
The area of the rectangle is 68.75cm^2''' | ''''''
```

## answers.py
This is where you want to put your python solution. This is used to compare answers and to create expected output where necessary.

## feedback.txt
this is general feedback for the question. No matter if they're right or wrong this will be shown.

## answers.toml
Similar to testcases except
```toml
[[answers]]
fraction = 75 | any number out of 100
text = "answer text"
feedback = "Feedback for Answer if selected"
```

## Supporting files
all supporting files are put in a child folder of the question. these can be any file types, but image types are added to the prompt otherwise they're just included files.


## Example usage
I have a Script I'm going to use to interact with the FiNoodle Package names testing.py
```py
from FiNoodle import exportQuestions as FiNoodle
import typer
from typer import Argument, Option

app = typer.Typer(
    add_completion=False,
)

@app.command(
    "build",
    help="Transpiles questions to Moodle XML",
)
def build():
    FiNoodle.build()
    
@app.command(
    "new",
    help="Generates a blank question template in the current working directory",
)
def new(
        qpath: str = Argument(
            ...,
            help="The question type to generate",
        ),
        name: str = Argument(
            ...,
            help="The name of the question to generate",
        ),
        qtype: str = Argument(
            ...,
            help="The question type to generate",
        ),
):
    FiNoodle.createBlankQuestion(qpath, name, qtype)
    print (f'new question created at questions/{qpath}')


if __name__ == '__main__':
    app()
```

running `python testing.py new Quiz1 Bananas cr`
A file structure is created as follows
```text
testing.py
questions
└──Quiz1
   └──Bananas.cr
      ├── Supporting Files
      ├── answer.py
      ├── prompt.md
      └── testcases.toml
```
After writing the question into answer.py, prompt.md and writing testcases, I can 
now run `python testing.py build` or execute `FiNoodle.build()` to generate an out.xml file which can be directly imported to Moodle as it's valid Moodle XML

<br>

### Supported File Types
* `.py`: Python programs
* `.md`: Prompt messages
* `.toml`: Test cases
* `Folders`: Supporting files (including images)

<br>

### Supported Question Types
* `.cr`: CodeRunner
* `.mc`: Multiple choice
* `.sa`: Short answer
* `.de`: Description

<br>
<hr>
<br>

<!-- REQUIREMENTS -->
## Requirements
* Markdown~=3.3.7
* Jinja2~=3.1.2

<br>
<hr>
<br>

<!-- FUTURE PLAN -->
## Future Plan
* Question repository: Managing and loading questions from external sources.
* More question types: Filling the blanks.
* More error checking: Duplicated questions.

<br>
<hr>
<br>

<!-- THE TEAM -->
## The Team
* Carl Taka
* Mongkulviseth Rithy
* Sam Shoykhet
* Sambav Ravivenkatesh
* Shejie Shuang
* Yunu Choi

<br>

* Trello board: https://trello.com/b/4HmtI49x/399-project-kanban

<br>
<hr>
<br>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* Toodle (<a href="https://github.com/James-Ansley">@James-Ansley</a>): https://github.com/James-Ansley/moodle-toml
* Best-README-Template : https://github.com/othneildrew/Best-README-Template