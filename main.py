from question_model import Quiz
from data import question_data
from quiz_brain import QuizBrain

questions = []

for i, question in enumerate(question_data):
    question_t = question["text"]
    question_a = question["answer"]
    new_q = Quiz(question_t, question_a)
    questions.append(new_q)

print(questions)

quiz = QuizBrain(questions)

while quiz.has_questions():
    quiz.next_question()
    print(f"Your score in this quiz is: {quiz.score} / {quiz.q_number}")