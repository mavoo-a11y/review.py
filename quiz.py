questions = ("Who is the Richest Man on Earth?",
             "Which is the most expensive car?",
             "Which is the most expenzive watch?",
             "How much is B2B worth?")

options = (("A. Elon Musk","B. Jeff Bezos", "C. Bill Gates", "D. Warren Buffet"),
           ("A. Bugatti Veyron", "B. Rolls Royce", "C. Lamborghini", "D. Ferrari"),
           ("A. Rolex", "B. Richard mille","C. Omega", "D. Casio"),
           ("A. 100 Billion", "B. 200 Billion", "C. 2 Billion", "D. 1 Billiom"))

answers = ("A", "A", "B", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print(" --------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
            score += 1
            print("Correct!")
    else:
            print("Incorrect!")
            print(f"{answers[question_num]} is the correct answer ")
    question_num += 1

# print("\n---------- RESULTS ---------")
print("Correct answers: ", end= " ")

for answer in answers:
                print(answer, end= " ")
                print()

                print("guesses: ", end= " ")
# for guess in guesses:
#                 print(guess, end= " ")
#                 print()

score_percent = int(score / len(questions) *100)
print(f"Your score is {score_percent}%")


