#asking the questions
#checking if the answer was correct
#checking if we are at the end of the quiz


class QuizBrain:
    def __init__ (self, q_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = q_bank
    
    #method
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):\n")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.title() == correct_answer:
            self.score += 1
            print("Your answer is correct.")
        else:
            print("Your answer is wrong.")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")
        
