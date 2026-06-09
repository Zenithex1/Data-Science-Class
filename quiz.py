quiz = {
    "What is the capital of Nepal?": "KATHMANDU",
    "What is the capital of Japan?": "TOKYO",
    "How many days are there in a week?": "7",
    "Which planet is known as the Red Planet?": "MARS",
    "What is 5 + 7?": "12",
    "What is the largest ocean on Earth?": "PACIFIC",
    "Who wrote Romeo and Juliet?": "SHAKESPEARE",
    "What is the chemical symbol for water?": "H2O",
    "Which animal is known as the King of the Jungle?": "LION",
    "How many continents are there?": "7"
}

# for question,answer in quiz.items():
#     print(question,answer)

import random

while True:
    question = random.choice(list(quiz.keys()))
    print(question)
    user_answer = input("Enter your answer: ")    