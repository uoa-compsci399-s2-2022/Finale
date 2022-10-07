from pathlib import Path
from moodle_compile.setup import importQuestions

def main():
    #targeted export by glob & exclusion by glob
    #export Children decides whether or not you want to export 
    #children of glob pattern category
    #make sure blackListGlob isn't accidentally blacklisting everything
    #use Null to match with nothing and "" to match with everything
    globPattern = {
        "exportGlob": "",
        "blackListGlob": "Null",
        "IterateChildren": False
    }
    

    root = Path("questions")
    xml = importQuestions(root, globPattern)
    with open("out.xml", "w") as f:
        f.write(xml)

if __name__ == '__main__':
    main() 