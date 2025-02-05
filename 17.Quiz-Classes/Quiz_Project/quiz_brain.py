# question_number = 0
# questions_list

#method next_question()

class QuizBrain: 
    def __init__(self, question_list): 
        self.question_number = 0
        self.question_list = question_list


    def still_has_questions(self): 
        #returns boolean depending on the value of question_number
        """Use len() method to dynamically calculate size of question_data instead of hardcoded at 12"""
            # if self.question_number > 12: 
            #     return false
            # else: 
            #     return true
        """Simply these four lines of code into one below"""    
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     False
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        #So current_question is a Question object and has text and question attributes

        #question number will start at 0 so either do + 1
        # input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ")
        
        #or better solution, += 1
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")



