from pathlib import Path
from Moodle_Toml import Quiz

def main():
    root = Path("questions")
    xml = Quiz(root)
    with open("out.xml", "w") as f:
        f.write(xml)

if __name__ == '__main__':
    main()