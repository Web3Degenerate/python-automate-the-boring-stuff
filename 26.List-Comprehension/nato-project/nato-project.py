# setup (Sec 26, V. 201 and V. 202)

'''Format for iterating over a df'''
for (index, row) in student_data_frame.iterrows(): 
    if row.student == "Angela":
        print(row.score)

'''Now becomes: '''
{new_key:new_value for (index, row) in df.iterrows()}


# TODO 1: Create a dictionary in this format: 
# { key:value}
# {"A": "corresponding code for NATO alphabet"}
# {"A": "Alfa", "B": "Bravo", etc. }

'''Reminder data_frame.to_dict() doesn't give us that sweet format we're gonna need'''


# TODO 2: Create a list of the phonetic code words from a word that the user inputs. 

# Solution: Enter word "TOM" outputs ['Tango', 'Oscar', 'Mike']
