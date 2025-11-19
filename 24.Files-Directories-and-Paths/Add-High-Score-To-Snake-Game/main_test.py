# file = open("my_file.txt")
# contents = file.read()
# print(contents)


# file.close() #manually close the file. # close the file after finished so it doesn't take up additional resources. 

# Avoid having to use open and close with the keywords `with` and `as`

with open("my_file.txt") as file:
    # file = open("my_file.txt")
    contents = file.read() #save contents in variable `contents`
    print(contents)

# close the file after finished so it doesn't take up additional resources. ls
# file.close() #manually close the file. 


## WRITE to file
# by default open("file.txt", mode=r), thus read only
# with open("my_file.txt") as file: #this opens the file in read-only mode
#     file.write("New text.")

# Change the mode to editable with mode=w
# This overwrites the old text
# with open("my_file.txt", mode="w") as file: #this opens the file in read-only mode
#     file.write("New REPLACEMENT text.")

# Append Mode
# Append Mode
with open("my_file.txt", mode="a") as file: #this opens the file in read-only mode
    file.write("\nNew APPENDED text.")

#
#
#
#
# IF YOU OPEN a file that doesn't exist IN WRITE (mode=w) mode, it will create it for you
with open("new_file.txt", mode="w") as file: #this opens the file in read-only mode
    file.write("Created with open() in mode=w aka write mode.")