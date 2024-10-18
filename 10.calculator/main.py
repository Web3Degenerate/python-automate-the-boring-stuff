import calcart

def subtract(n1, n2): 
    return n1 - n2

def add(n1, n2): 
    return n1 + n2

def multiply(n1, n2): 
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Store each function in an operations dictionary: (without triggering ie add() )
operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide,
}

# Use the dictionary operations to perform the calculation: 

# multiply
# print(operations["*"](4,2))

# use recursion
def calculator():
    # if using ascii art import here with print(art.logo)
    print(calcart.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?"))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number? "))

        # Pass in the user selected math operation saved in 2nd input to variable operation_symbol
        # print(operations[operation_symbol])

        # Then trigger the function with () and pass in our float input variables above as num1 and num2
        # print(operations[operation_symbol](num1, num2))

        # Clean up the result with an f string
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start over.")

        if choice == "y":
            num1 = answer
        else: 
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()