
# Creating new list (Old way)
numbers = [1, 2, 3]
# new_list =[]
# for n in numbers:
#     new_list.append(n + 1)


'''List Comprehension format:
new_list = [new_item for item in list]'''
new_list = [n+1 for n in numbers]


print(new_list) #[2, 3, 4]

'''STRING example'''
name = "Angela"
letters_list = [n for n in name] #[letter for letter in name]
print(letters_list) # returns ['A', 'n', 'g', etc]


'''Range example'''
my_range = range(1,5)
new_range = [n*2 for n in my_range]
print(new_range) #returns 2, 4, 6, 8



## CONDITIONAL LIST COMPREHENSION **********************************************

# FORMAT: add `if test` at end
# new_list = [new_item for item in list if test]

test_range = range(1,11)
evens_in_test_range = [num for num in test_range if num % 2 == 0]
print(evens_in_test_range) #returns [2, 4, 6, 8, 10]

#same with list of sting names of various lenghts in list called names
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)

# IF test matched, use first keyword to perform an action on the passing data
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)