class QuizBrain():

    def __init__(self, q_list):
        self.q_number = 0
        self.score = 0
        self.q_list = q_list

    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        answer = input(f"Otázka č. {self.q_number}: {current_question.question_text} (True/False): ")
        self.check_answer(answer, current_question.question_answer)

    def check_answer(self, user_answer, original_answer):
        if user_answer.lower() == original_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Sorry, try again!")
        print(f"The correct answer was: {original_answer}")

    def has_questions(self):
        if self.q_number < len(self.q_list):
            return True
        else:
            return False



