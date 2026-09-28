questions = [
    {
        "question": "What is the capital of France?",
        "answer": "paris"
    },
    {
        "question": "What is 5 + 3?",
        "answer": "8"
    },
    {
        "question": "What programming language are we using?",
        "answer": "python"
    },
    {
        "question": "How many days are there in a week?",
        "answer": "7"
    },
    {
        "question": "What keyword is used to define a function in Python?",
        "answer": "def"
    }
]


def play_quiz():
    score = 0

    print("=== QUIZ GAME ===")
    print("Answer each question.\n")

    for number, item in enumerate(questions, start=1):
        print(f"Question {number}:")
        print(item["question"])

        user_answer = input("Your answer: ")

        if user_answer.lower().strip() == item["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!")
            print("Correct answer:", item["answer"])
            print()

    print("=== QUIZ FINISHED ===")
    print("Your score:", score, "/", len(questions))


def main():
    play_quiz()


if __name__ == "__main__":
    main()
