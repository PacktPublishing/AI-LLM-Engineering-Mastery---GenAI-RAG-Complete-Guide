import json
from pathlib import Path

# JSON - Javascript Object Notation
# names = ["James", "Ruth", "Mary"]
# with Path.open("names.json", "w") as file:
#     contents = json.dumps(names)
#     file.write(contents)

with Path.open("names.json", "r") as file:
    contents = json.load(file)
    print(contents[0])
