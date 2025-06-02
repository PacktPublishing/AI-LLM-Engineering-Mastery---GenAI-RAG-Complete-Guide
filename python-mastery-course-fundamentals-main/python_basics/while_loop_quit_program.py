# counter = 0
# while counter < 5:
#     print(f"Counter is {counter}")
#     counter += 1

prompt = "\nEnter 'quit' to end the program."
prompt += "\nEnter your command:"

while True:
    command = input(prompt)

    if command == "quit":
        break  # exit this loop
    else:
        print(f"You've entered: {command}")
