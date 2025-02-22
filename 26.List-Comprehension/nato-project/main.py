import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
# format: 
# {row.letter:new_value for (index, row) in data.iterrows()}
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)


#TODO 2. Take user input and check it against each key in the dictionary
word = input("enter a word: ").upper()
# Format: 
# [new_item for item in list]
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
