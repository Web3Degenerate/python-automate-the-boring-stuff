from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# Loop through the question_data list of dictionaries and add to our question_bank LIST (array)

"""1. Write a for loop to iterate over the question_data"""

"""
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

"""



question_bank = [] #Create List (array)
for x in question_data:
    x_text = x["text"]
    x_answer = x["answer"]
    """2. Create a Question object from each entry in question_data"""
    new_question = Question(x_text, x_answer)
    """3. Append each Question object to the question_bank"""
    question_bank.append(new_question)


# print(question_bank) #will return a list of question objects [<Object>, <Object>, etc.]

# Drill down into List of Questions Objects: 
print(f'First Question: {question_bank[0].text} \n First Answer: {question_bank[0].answer}')


# In Sec 17 - V.122 - Create a new QuizBrain Object
quiz = QuizBrain(question_bank)
# quiz.next_question()
 
# In at Sec 17 - V.123.
# while quiz.still_has_questions: # FORGOT () FOR METHOD!!
while quiz.still_has_questions():
    quiz.next_question()


# Resume at Sec 17 - V. 124 - Check answers