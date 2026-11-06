import random

# Quiz Application - Python Project

questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. def", "C. function", "D. define"],
        "answer": "B"
    },
    {
        "question": "What is the output of len('Hello')?",
        "options": ["A. 4", "B. 5", "C. 6", "D. 3"],
        "answer": "B"
    },
    {
        "question": "Which data type is mutable in Python?",
        "options": ["A. Tuple", "B. String", "C. List", "D. Integer"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. #", "B. //", "C. /*", "D. &"],
        "answer": "A"
    },
    {
        "question": "Which function displays output in Python?",
        "options": ["A. input()", "B. print()", "C. show()", "D. display()"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. int", "B. str", "C. bool", "D. list"],
        "answer": "C"
    },
    {
        "question": "Which loop runs while a condition is true?",
        "options": ["A. for", "B. while", "C. if", "D. def"],
        "answer": "B"
    },
    {
        "question": "Which brackets are used to create a list?",
        "options": ["A. ()", "B. {}", "C. []", "D. <>"],
        "answer": "C"
    },
    {
        "question": "Which method adds an element to a list?",
        "options": ["A. append()", "B. remove()", "C. upper()", "D. split()"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used for an additional condition?",
        "options": ["A. else if", "B. elif", "C. repeat", "D. next"],
        "answer": "B"
    }
]


def run_quiz():
    score = 0
    review = []

    quiz_questions = random.sample(questions, 5)

    print("\n====================================")
    print("       PYTHON QUIZ APPLICATION")
    print("====================================")

    name = input("\nEnter your name: ")

    print(f"\nWelcome, {name}!")
    print("Answer each question using A, B, C or D.")

    for number, question in enumerate(quiz_questions, 1):

        print(f"\nQuestion {number}/5")
        print(question["question"])

        for option in question["options"]:
            print(option)

        while True:
            answer = input("Your answer: ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break

            print("Invalid input! Please enter A, B, C or D.")

        correct_answer = question["answer"]

        if answer == correct_answer:
            print("Correct answer!")
            score += 1
        else:
            print(f"Wrong answer! Correct answer: {correct_answer}")

        review.append((number, answer, correct_answer))

    percentage = (score / 5) * 100

    print("\n====================================")
    print("             QUIZ RESULT")
    print("====================================")

    print(f"Student Name: {name}")
    print(f"Total Questions: 5")
    print(f"Correct Answers: {score}")
    print(f"Wrong Answers: {5 - score}")
    print(f"Final Score: {score}/5")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    print("\n--------- ANSWER REVIEW ---------")

    for number, given, correct in review:
        status = "Correct" if given == correct else "Incorrect"
        print(f"Q{number}: Your answer: {given} | Correct: {correct} | {status}")

    print("\nThank you for participating!")


if __name__ == "__main__":
    run_quiz()