#return capital case, first letter capitalized

################## title() function ###################
def format_name(f_name, l_name):
        # print(f_name.title())
        # print(l_name.title())

    # if either input is missing, escape the function:    
    if f_name == "" or l_name == "":
        # return #returns #none
        return "You did not return a valid input."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    # print(f"Hello {formatted_f_name} {formatted_l_name}, how are you?")
## USE RETURN INSTEAD
    return f"Hello {formatted_f_name} {formatted_l_name}, how are you?"

# formatted_string = format_name('edward', 'McDooGle')
# print(formatted_string)
print(format_name(input("What is your first name?"), input("What is your last name?")))

############ Pass another function as the parameter in the function call: #########

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1('hello'))
print(output)