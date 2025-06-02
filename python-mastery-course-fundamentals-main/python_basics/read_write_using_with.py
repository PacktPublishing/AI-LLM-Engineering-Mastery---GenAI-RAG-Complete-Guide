from pathlib import Path


with Path.open("example.txt", "w") as file:
    contents = file.write("This is all new to me!!")

    print(contents)
