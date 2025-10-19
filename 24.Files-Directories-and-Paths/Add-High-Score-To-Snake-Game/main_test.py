# file = open("my_file.txt")
# contents = file.read()
# print(contents)


# file.close() #manually close the file. # close the file after finished so it doesn't take up additional resources. 

# Avoid having to use open and close with the keywords `with` and `as`

with open("my_file.txt") as file:
    # file = open("my_file.txt")
    contents = file.read()
    print(contents)

# close the file after finished so it doesn't take up additional resources. 
# file.close() #manually close the file. 
# file.close() #manually close the file. 
# file.close() #manually close the file. 
