questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
}

score = 0
total_questions = len(questions)
print("Welcome to the Quiz Game!")
print("Type 'quit' at any time to exit \n")

for question, correct_answer in questions.items():
    user_answer = input(question + "")

    if user_answer.lower() == "quit":
        break
    elif user_answer.lower() == correct_answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {correct_answer}")

    print()

print(f"Quiz completed. Your score is {score}/{total_questions}")
