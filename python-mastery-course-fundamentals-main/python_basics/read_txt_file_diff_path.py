from pathlib import Path

path = Path("example.txt")
path = Path("./python_basics/example.txt")


contents = path.read_text()

print(contents.lower())
