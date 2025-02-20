

#Randomly assign scores
import random

#Names List
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# FORMAT: 
# student_scores = {new_key:new_value for student in LIST}

#=================================================================
#============== Dictionary Comprehension From a List =============
#=================================================================
'''Iterate over a List ['Alex', 'Beth', 'Caroline', etc]'''

# Student_Scores Dictionary
'''Here, student is the key: and random test score is the value '''
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)



#=================================================================
#============== Dictionary Comprehension From a Dictionary =============
# ============= DICTIONARY.items()
#=================================================================
'''Iternate over dictionary {'Alex': 70, 'Beth': 9, 'Caroline': 93, etc.}'''

# Passed Students Dictionary
# Format:         
# passed_students = {new_key:new_value for (key, value) in DICTIONARY.items()}
# passed_students = {student:score for (student, score) in student_scores.items()}

# Plus add in our IF condition at the end
# passed_students = {new_key:new_value for (key, value) in DICTIONARY.items() if test}
passed_students = {student:score for (student, score) in student_scores.items() if score > 50}

print(passed_students)