 # Sec 27 - V.206 - Setting Default Values for Optional Arguments

# Unlimited Arguments Example: 

def add(*args):
    print(args)

add(3, 5, 6) # jjust prints 3, 5, 6 on SAME line


def add_for_loop(*args):
    for n in args:
        print(n)


add_for_loop(3, 5, 6) # prints 3, 5, 6 on new line each


# *args creates a tuple of your input, so here (3, 5, 6)
def add_actual(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


add_actual(3, 5, 6) # returns 14...if you `return sum` ;)

# Double askteriks ** "kwargs" (keyword arguments)
# pass in n, the normal positional argument
def kwargs_calculate(n, **kwargs):
    print(kwargs)
    #loop through dictionary standard method
    for key, value in kwargs.items():
        print(key)
        print(value)
    # or just pull the value we want, here the 3 value to key 'add'
    print(kwargs["add"]) #returns 3
    # add and multiply to the value of n
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n) #2+3 = 5, 5*5 = 25


kwargs_calculate(2, add=3, multiply=5) #returns dictionary {'add': 3, 'multiply': 5}



#S27. V208.
class Car: 

    def __init__(self, **kw):
        # this would REQUIRE value for make / model
        self.make = kw["make"]
        self.model = kw["model"]
        '''Use .get() to make make/model optional'''
        self.make = kw.get("make")
        self.model = kw.get("model")      

your_car = Car(make="Nissan", model="GT-8")
print(your_car.make)
print(your_car.model)

my_car = Car(make="kia")
print(my_car.make)
print(my_car.model) #returns 'none' instead of an error