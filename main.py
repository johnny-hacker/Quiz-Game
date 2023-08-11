from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# parse through data dictionary
for each_question in question_data:
    # assign a text and answer variable for each one
    text = each_question["question"]
    answer = each_question["correct_answer"]
    # append each question to the question bank
    question_bank.append((Question(text, answer)))

# create a new instance of the Quiz brain that will display question number and grab user input
quiz = QuizBrain(question_bank)
# evaluate the still has question method to verify that the question bank still has questions
while quiz.still_has_question():
    # proceed to the next question
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your Final Score is {quiz.score}/{quiz.question_number}")

