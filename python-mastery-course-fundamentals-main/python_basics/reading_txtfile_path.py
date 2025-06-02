from pathlib import Path

path = Path("example.txt")


contents = path.read_text()

print(contents.lower())
