from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from os import system
from art import logo


question_bank= []
for question in question_data: 
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

system('clear')
print(logo)
while quiz.still_has_questions():
    quiz.next_question()


