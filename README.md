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


## Open tdb Trivia API [OpenTDB.com](https://opentdb.com/api_config.php)
- Select question number, type, etc. and select **Generate API URL**
- Get something like `https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean` 

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


### Importing Modules (S18.V130)

**Basic Import**
- **Keyword** + **Module name**
- from turtle

- Then you invoke a class with:

- `timmy = turtle.Turtle()` 


**Import with From**

- **Keyword** + **Module name** + **keyword** + **Thing in Module**
- from turtle import Turtle

- Then you invoke an object with: 

- `timmy = Turtle()` 


**Import All with From**
- **Keyword** + **Module name** + **keyword** + **Thing in Module**
- from turtle import *


**Import Alias (makes more sense with longer module names)**
- import turtle-asd_fgh_asdf_asd as t
- `timmy = t.Turtle()` 


### Installing Modules

- Some modules can't be imported **because they are not packaged with the standard python code**
- So install them with `pip` from [pypi.org](https://pypi.org)
- Example: [**heroes 1.0.2**](https://pypi.org/project/heroes/)


- installing a package, installs it in your local working python environment. 
- This is on a per project basis. 
- Get's stored in `.venv/lib/python3.X/` in pycharm or `.venv/lib/` in VS directory, your virtual environment. 


**The need for Virtual Environments**
- Python 3 is not backwards compatible with Python 2. 
- Virtual environments create a small sandbox for our project
- Avoids global conflicts over time


**RESUME AT SEC 18, V.134 Python Tuples and Generate random RGB colors**

S18.V.134 - **Python Tuples**
- CAN NOT CHANGE values in a Tuple (No item assignment)

```py

#Tuple (ordered)
my_tuple = (1, 3, 8)
my_tuple[0] #retrieves first item, here 1
#can't change tuple vlaue
my_typle[1] = 12 #returns error: 'tuple' object not support item assignment

#List
my_list = [1, 3, 8]

```


---


19. 



---

20. 


---

21. 


---


22. 


---


23. 


---


24. 


---


### 25. CSV Data and Pandas 


- Download [the sample csv data from this link](https://docs.google.com/spreadsheets/d/1Rs1CKjiagTeXa53212JkjRSDu-tx77_YxEgGdkv5zRY/edit?gid=0#gid=0). 
- Save as `weather_data.csv` 


### Importing the CSV data

1. One option is with .readlines() but this will be harder to parse later

```py
# use readlines() method to create a list named data from values in weather_data.csv
# Use relative file path (same directory) to read weather_data.csv

with open("weather_data.csv") as data_file: 
    """Use readlines() not just read() to get each line as item in our list"""
    data = data_file.readlines()
    print(data)

    # Returns our list: 
    #['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 
    # 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 
    # 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']

```

2. Second option is to use the built in `csv` module: 

```py
import csv

with open("weather_data.csv") as data_file: 
    data = csv.reader(data_file)
    print(data)
    # This creates a CSV READER Object
    # <_csv.reader object at 0x000002126E0B7640>

    """The CSV Reader Object can be LOOPED through"""
    # each csv item is a single value
    # The temperatures is in ROW index 1
    temperatures = [] #empty temperatures list
    for row in data:
        if row[1] != "temp": #exclude the headers 
            #Add each temperatures aka row index 1 to our list and convert to int
            temperatures.append(int(row[1]))
    print(temperatures)
    
    #returns [12, 14, 15, 14, 21, 22, 24]

```


## Pandas Python Data Analysis Library Visit [Pandas.pydata.org](https://pandas.pydata.org/docs/getting_started/index.html)

- Helpful in particular with tabular data like our csv example. 

- Pandas not built into python. Have to install it. 

### Installing Pandas
- You can install pandas from [PyPi.org at this link here](https://pypi.org/project/pandas/).

- Run command `pip install pandas` 


#### Panda Data Structures

**two primary data structures in pandas**
- 1 - Series (1-dimensional) - **like single column of csv**
- 2 - DataFrame (2-dimensional) = **like our csv table data**


```py
import pandas

data = pandas.read_csv("weather_data.csv")
print(data) #prints out much better
print(type(data)) # returns DataFrame: <class `pandas.core.frame.DataFrame`>

print(data["temp"]) #just prints out temp column
print(type(data["temp"])) # returns Panda Series <class `pandas.core.series.Series`>

```

- See [**Pandas API Reference Here**](https://pandas.pydata.org/docs/reference/series.html)


### Pandas Built in Methods

**Average with .mean()**
- Example with Average. (No average method in python)

```py
# [Average in Python] https://www.geeksforgeeks.org/find-average-list-python/
avg = sum(temp_list) / len(temp_list)

# Average with Pandas' built-in method .mean()
data["temp"].mean()
print(f'Mean with Panda .mean() method is: {data["temp"].mean()}')

```

**To Dictionary or To List**

```py
# Turn DataFrame into a Dictionary with Method to_dict()
data_dict = data.to_dict()
print(data_dict)

# Turn Series into a List with Method to_list()
temp_list = data["temp"].to_list()
print(temp_list)
# Then you can do all the things you can with a list, like return the length - len()
print(f"The size of this list series is {len(temp_list)}")

```

### Pandas calling csv headers (CASE SENSITIVE!)

**TWO was to call csv headers**
- 1. `data["temp"]`
- 2. `data.temp`


### Pandas- Create Custom DataFrame and save to csv with .to_csv(<path><name>) 


```py

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}


# Call our pandas library and then our DataFrame Class
new_df = pandas.DataFrame(data_dict) # initalize that df class with our data_dict data
print(new_df)


## NOW WE CAN CONVERT OUR new_df DataFrame to csv with the .to_csv() method
# Just needs the required param of the path you want to save csv file to.

# SAME directory, just give it a name
new_df.to_csv("new_df.csv")

```


---

26. 

---
### Note on git merge

- _Fell behind current state and tried to push up changes. (2/8/25)_
- Followed these commands from [freecodecamp article](https://www.freecodecamp.org/news/git-pull-force-how-to-overwrite-local-changes-with-git/)

1. `git fetch`
2. `git reset --hard HEAD`
3. `git merge origin` 
    - this returned error message, and then followed conflict manager in VS code