student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items(): 
    print(key)
    # print(f"student key: {key} and value: {value}.")


#=============================================================================================
#======= Iterating over Pandas DataFrame PRETTY MUCH the same as Python Dict =================
#======= just use .items() on DataFrame like regular Dictionary
#=============================================================================================

import pandas

# Create new DataFrame from our student_dict
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)


#Loop through a data frame the ole fashion way = MESSY
# loops through names of columns and then data, 
for (key, value) in student_data_frame.items(): 
    print(value) 



#=============================================================================================
#======= Pandas DataFrame IN BUILT LOOP WITH == .iterrows() instead of .items() =================
#=============================================================================================
# Sec 26. V. 200

                               '''    .iterrows() instead of .items()  '''
for (index, row) in student_data_frame.iterrows(): 
    print(index) #prints DataFrame, then each index number
    
    print(row) #prints out each row, bit sloppy tho

    '''Each row is a Pandas Series Object, so we can access info with dot notation'''
    print(row.student) #prints out DataFrame, then each student value (Angela, James Lilly)

    print(row.score) #same for the score values

    '''Use Conditional logic to only print Angela's Score'''
    if row.student == "Angela": 
        print(row.score)

