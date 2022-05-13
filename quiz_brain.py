class QuizBrain:   # Create class
    def __init__(self, q_list):
        self.question_number = 0       # set attribute to default 0 since ques starts from 0
        self.question_list = q_list
        self.score = 0                 # Create score attribute which will have default 0 value

    def next_question(self):
        current_question = self.question_list[self.question_number]    # get hold of current question and answer text, using list indexing
        self.question_number += 1     # add 1 to ques number after every turn
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")    # Set user's input as variable, which will be assigned to the parameter of following function
        self.check_answer(user_answer=user_answer, correct_answer=current_question.answer)

    def still_has_questions(self):     # check if all the ques have been shown
        return self.question_number < len(self.question_list)    # returns True if haven't reach the total no. of ques, False otherwise

    def check_answer(self, user_answer, correct_answer):      # check if user answer is same as actual answer
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}. ")  # This will be printed for both right and wrong
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")        # This will add a empty line between each question




