class QuizBrain:
    # initialize the class
    def __init__(self, q_list):
        # question number will keep track of which question the quiz is on
        self.question_number = 0
        # question list will hold the list of questions initialized by main.py via dictionary of questions/answers
        # in the data.py
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        # if the question number is less that the length of all questions in the q_list
        # it will return, if not the method will not return
        return self.question_number < len(self.question_list)


    def next_question(self):
        # set a placeholder for each question
        current_question = self.question_list[self.question_number]
        # increase the question number every times its called
        self.question_number +=1
        # retrieve user input
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, u_answer, q_answer):
        # if the user answer is the same as the question answer
        # update score and let the user know if they were right or wrong
        if u_answer.lower() == q_answer.lower():
            self.score +=1
            print("correct!")
        else:
            print("sorry, that's incorrect :(")
        # tell them what the correct answer was
        print(f"the correct answer was: {q_answer}")
        # check the score
        self.check_score(self.score)


    def check_score(self, score):
        # print the score
        return print(f"Your current score is {self.score}/{self.question_number}\n")
