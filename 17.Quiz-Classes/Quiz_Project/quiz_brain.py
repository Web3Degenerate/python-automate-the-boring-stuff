# question_number = 0
# questions_list

#method next_question()

class QuizBrain: 
    def __init__(self, question_list): 
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        #So current_question is a Question object and has text and question attributes

        #question number will start at 0 so either do + 1
        # input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ")
        
        #or better solution, += 1
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")