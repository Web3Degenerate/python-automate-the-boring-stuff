### List of helpful functions

1. len()

2. str() and int()

...

3. title() - Uppercase first letter of each word

```py

def function(text):
    return text.title()

```

4. Append method
   `correct_letters_list.append(letter)`

---

5. Index
   `alphabet.index(letter)`

---

6. choice() with import random

```python

import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
card = random.choice(cards)

```

---

7.  Use \_ in loop instead of rando variable:

    """If you don't need a variable you can use an underscore _ """
    for _ in range(2):

---

8. The **global** keyword to import global sccope into a function

```py

enemies = 1


def increase_enemies():
    global enemies # USE GLOBAL KEYBOARD to change our global variable `enemies`
    # enemies = 37
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
```

---

9. [ASCII Art generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)

---

10. From random module import `randint`

```py
from random import randint

```

---

11. Run [your python code through Python Tutor](https://pythontutor.com/visualize.html#mode=edit) to see it run step by step.

Shown in **_See Video 92. - 12.Number-Guessing-Game/number_guessing.py_**

---

12. Reminder, you can just use the `return` key to exit a function if desired
    **_See 12.Number-Guessing-Game/number_guessing.py_**

---

13. Set user input to all lower case with `.lower()`

```py
guess = input("Who has more followers, Type 'A' or 'B': ").lower()

```

14. In 15.Coffee-Machine/coffee.py we used the round function:

```py
change = round(money_received - drink_cost, 2)

```

---

15. Import portion of external module (_Turtle module in lesson 16_)

```py
#Alternatively, use from - import just the Turtle class
from turtle import Turtle

# Use parenthesis to actually construct the turtle object
timmy = turtle.Turtle()

print(timmy) #prints object <turtle.Turtle object at 0x0000026AD0848F10>

```

---

16. Python Packages at [pypi.org](https://pypi.org/)

_See video 111 (section 16)_, introducing pypi.org packages.

import the [PrettyTable](https://pypi.org/project/prettytable/) ascii table plugin

with: `pip install PrettyTable` 

Get the [Coffee Machine OOP start code here](https://replit.com/@appbrewery/oop-coffee-machine-start)

**While Loop Logic for Coffee Machine OOP**

```py

money_machine = MoneyMachine()

coffee_maker = CoffeeMaker()

coffee_maker.report()
money_machine.report()

#resume at Sec 16, v.114 at (3:53)

# set up while loop to handle the condition when coffee machine is on
is_on = True
menu = Menu()

while is_on: 
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else: 
        #check that we have enough resources for the selected drink with find_drink(order_name) method
        drink = menu.find_drink(choice)
        print(drink)

```

---


17. Quiz Class

**To create an empty class** use the **pass** keyword

```py
class User:
    """To create an empty class, use the pass keyword"""
    pass


user_1 = User()

```

**Naming Conventions**
Classes use `PascalCase`. Pretty much everything else is `snake_case`. 

Python doesn't commonly use `camelCase`


### Class Constructors
- Constructor - what happen when object is created, hence when it is initialized. 
- use the init function, in python: 

```py
def __init__(self):

```


**In our User Example**

```py
class User:
    def __init__(self, user_id, user_name):
        # set up user id place holder
        self.id = user_id
        self.user_name = user_name
        # We can set up default values, like followers = 0
        self.followers = 0

```


### Method is a function attached to an object. 
_like in a class_ 

Our example of adding a method to simple User class and calling it on our first User object. 

```py


class User:
    def __init__(self, user_id, user_name):
        # set up user id place holder
        self.id = user_id
        self.user_name = user_name
        # We can set up default values, like followers = 0
        self.followers = 0
        #set up for method with two params example below
        self.following = 0

    #passing in self, when method is called, it knows which object called it.
    def new_followers(self):
        self.followers += 2

user_1 = User("01", "Al")
print(user_1.user_name)
user_1.followers = 1
print(f'{user_1.user_name} has {user_1.followers} followers') # 1 follower

#DON'T HAVE TO PASS IN SELF ie user_1.new_followers(user_1)
user_1.new_followers()
print(f'Now, {user_1.user_name} has {user_1.followers} followers') # 3 followers

```

### Example of method taking both self and user params

```py


    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Alba")
user_2 = User('002', 'Barbara')
user_1.follow(user_2) #implied (self/user_1, user_2)
print(f'Now, after method examples, {user_1.user_name} has {user_1.followers} followers and {user_2.user_name} has {user_2.followers} followers')
# Alba 0 followers
# Barabra 1 followers

```


---

18. **Turtle GUI Documentation** [_See methods & docs here_](https://docs.python.org/3/library/turtle.html#turtle-methods)

_Turtle model uses_ [TKinter documentation](https://docs.python.org/3/library/tkinter.html)


## for _ in range(x) loop
Here, do something 4 times: 

```py
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

```


### Importing Modules

**Basic Import**
- **Keyword** + **Module name**
- from turtle

- Then you invoke a class with:

- `timmy = turtle.Turtle()` 


- **Keyword** + **Module name** + **keyword** + **Thing in Module**
- from turtle import Turtle

- Then you invoke an object with: 

- `timmy = Turtle()` 

---