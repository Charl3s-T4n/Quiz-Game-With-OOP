from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []         # Create empty list so i can append each question object to it
for question in question_data:     # iterate over question_data
    new_question = Question(text = question["text"], answer = question["answer"])     # question in this case is a dictionary
    question_bank.append(new_question)   # append to empty list

quiz = QuizBrain(q_list = question_bank)

while quiz.still_has_questions():    # while True, user answered correctly
    quiz.next_question()  # .next_question() method of class QuizBrain will show user input
print("You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
