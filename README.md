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

## for \_ in range(x) loop

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
- from turtle import \*

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

S18.V.134 - **Python Tuples ()**

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

#### RGP challenge (rbg_example.py)

- create random int from the random module (`random.randint(0, 255)`)
- and use a custom function to generate a random color using the rgb values from 0 - 255

```py
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    '''GENERATE our Tuple with the random values for RGB'''
    # random_color = (r, g, b)
    # return random_color
    return (r, g, b)


```

#### Spirograph - for \_ in (range)

- for in range can only take integers
- division always returns float, even if whole number, ie 5.0

```py

def draw_spirograph(size_of_gap):
    '''(1) division always returns float, even if 10/2 = 5.0'''
    '''(2) range() only take int, so wrap division in int()'''
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100) #param is the radius size
            # print(tim.heading()) # returns 0.0
            # current_heading = tim.heading()
            # tim.setheading(current_heading + 10) #param takes angle
        # REFACTOR to one line:
        # tim.setheading(tim.heading() + 10)
        tim.setheading(tim.heading() + size_of_gap)

#call custom function with size_of_gap = 5
draw_spirograph(5)

```

#### In Sec 18. V136 (Hirst) installed python package

- Installed [colorgram.py](https://pypi.org/project/colorgram.py/)
- `pip install colorgram.py`

#### Modulo solution

- In [18.Turtle-GUI/Hirst-Painting-Project/main.py](https://github.com/Web3Degenerate/python-automate-the-boring-stuff/blob/main/18.Turtle-GUI/Hirst-Painting-Project/main.py) We needed a block of code to run when the dot count hit groups of 10, so 10, 20, 30, 40...70, 80, 90, 100.
- To triger this we used `if dot_count % 10 == 0:` where dot_count was incrementing from 1 to 100

```py

for dot_count in range(1, number_of_dots + 1): #range(1, 101) to get the last dot (100th dot)
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    '''Reset typewriter at end of each 'row', which is blocks of 10!! '''
    if dot_count % 10 == 0: #means count is 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
        '''We need this block to repeat after every row (typewriter reset)'''
        # Reset position outside of for loop which is just going across screen (left => right) 10 dots
        tim.setheading(90) #face up
        tim.forward(50) #move forward by 50 paces
        tim.setheading(180) #turn left at end of line
        tim.forward(500) # move 10 x 50 paces so 500 (go back to left like typewriter)
        tim.setheading(0) #turn right

```

### Get a List of Tuples

- In [18.Turtle-GUI/Hirst-Painting-Project/main.py](https://github.com/Web3Degenerate/python-automate-the-boring-stuff/blob/main/18.Turtle-GUI/Hirst-Painting-Project/main.py)
- Our desired data format: `#[(168, 99, 102), (168, 99, 102), (168, 99, 102), etc.]`
- However data was coming out `[Rgb(r=245, g=243, b=238), Rgb(r=247, g=242, b=244), etc]`
- Tuple solution below.

```py

rgb_colors = []
for color in colors:
    rgb_colors.append(color.rgb) #specify rgb or hsl etc.

# print(rgb_colors) returns [Rgb(r=245, g=243, b=238), Rgb(r=247, g=242, b=244), etc]

# So modify like so:
'''Solution to get format we need, change how we tap into data in for loop'''
formatted_rgb_colors = []
for c in colors:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    '''CREATE OUR TUPLE WITH DESIRED (R, G, B) VALUES'''
    new_color = (r, g, b)
    formatted_rgb_colors.append(new_color)

```

## x

## 19. Higher Order Functions - Don't use fun ()

- Calling one function from antoher

```py

# Calculator Function
def function_a(n1, n2, func):
    return func(n1, n2)

# Addition Function
def function_b(n1, n2):
    return n1 + n2

# Subtraction Function
def function_c(n1, n2):
    return n1 - n2


'''Function A is the higher order function b/c it takes other functions'''
#Pass functions b and c to a
function_a(function_b)
function_a(function_c)

```

### Turtle can add JavaScript like event listeners

- Sec 19. V. 140. See Turtle Docs
- See docs on [.onkey()](https://docs.python.org/3/library/turtle.html#turtle.onkey) and [.listen()](https://docs.python.org/3/library/turtle.html#turtle.listen)

---

20.

---

### 21. Slicing (piano_keys[2:5])

- See [Sec 21 V.158 on Slicing in Python](https://www.udemy.com/course/100-days-of-code/learn/lecture/20361177#overview)

- Slice Range does not include the last position `[2:5]`
- Slice to the end, omit the 2nd range number `[2:]`
- Slice Third number, specify which objects to select in given range `[2:5:2]`

```python

piano_keys = [0, 1, 2, 3, 4, 5, 6, 7, 8]

'''Returns 2, 3 and 4, NOT include 5'''
print(piano_keys[2:5])

'''OMIT 2nd Range Number - Returns 2, to 8'''
print(piano_keys[2:])

'''OMIT 1st Range Number - Returns 0 to 4'''
print(piano_keys[:5])

'''Third Number Which Objects To Take - Here Every Other Obejct '''
'''Returns 2, (skip 3) and 4'''
print(piano_keys[2:5:2])

'''Range = All, Selection = Every 2nd Item'''
'''Here, this would return all the odd numbers 1, 3, 5, 7'''
print(piano_keys[::2])


'''You can also use third number to flip the list with -1 '''
'''Here, this would return all the numbers flipped 8 to 0'''
print(piano_keys[::-1])

```

- In the Snake Game, we needed to skip the first section of the snake (head) and then process the rest of the snake body.

With slicing we could avoid using code like:

```py

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

```

And instead use:

```py

    ''' snake.segments[1:] which excludes first 0 item (head) '''
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

```

---

22. _Resume here_!



---

23.

---

24. Intermediate - Files and Directories. 

- See Sec 24, V.183 on the start of Open, Read and Write to Files using `with` Keyword

- Review notes on opening files for work.

- To Open a File with Python: 
- - x

- To Read a file with Python: 
-- y

- To Write to a file with Python: 
-- z

Resume at min 2:38.


- Open, Read and Write
-- key points: 


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

## Squirrel Data Project

- Download the squirrel csv file from [data.cityofnewyork.us](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data)

- Save CSV file as `squirrel_count_raw.csv` in project folder.

- Import pandas and pull in the raw data with

```py
import pandas
data = pandas.read_csv("squirrel_count_raw.csv")

```

### Turn a column in our csv data into a list with pandas .to_list()

- call the `to_list()` function on our column
- This allows us to use things like `for .. in  x`

```py

import pandas
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

'''USE of if .. in is available ONLY because it has been converted into a LIST'''
if answer_state in all_states:

    t = turtle.Turtle()
    t.hideturtle() # hide it
    t.penup() #no drawingour states table
    state_data = data[data.state == answer_state]
    t.goto(state_data.x.item(), state_data.y.item()) #move turtle to x, y coordinates of state
    t.write(answer_state) #since we already verified user input above, use it to print


```

#### Pandas .item() [_see pandas.Series.item docs here_](https://pandas.pydata.org/docs/reference/api/pandas.Series.item.html)

- we used .item() to get a single text value from our csv table as shown below:

```py

#Instead of t.write(answer_state)
t.write(state_data.state.item())

```

#### Break statement in our while loop with `for in` and `for not in`

- Create a list of states not answered correctly
- Break out of the while loop when user input = `Exit`
- use `.title()` output for force any input to first letter upper case
  -- such as `DeLaWarE` to be `Delaware`
- Finally, convert our new list of missed states to a DataFrame
- Export this missing states list to a csv file in the same directory

```py
    # BREAK out of while loop when user input = 'Exit'
    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        # Turn missing_states list into a DataFrame
        new_data = pandas.DataFrame(missing_states)
        # Export to CSV in same directory
        new_data.to_csv("states_to_learn.csv")
        break

```

---

## 26. List Comprehension

#### Python Sequences

- list
- range
- string
- tuple

### List Comprehension format:

```py
# Creating new list (Old way)
numbers = [1, 2, 3]
# new_list =[]
# for n in numbers:
#     new_list.append(n + 1)

'''List Comprehension format:
new_list = [new_item for item in list]'''
new_list = [n+1 for n in numbers]


'''STRING example'''
name = "Angela"
letters_list = [n for n in name] #[letter for letter in name]
print(letters_list) # returns ['A', 'n', 'g', etc]


'''Range example'''
my_range = range(1,5)
new_range = [n*2 for n in my_range]
print(new_range) #returns 2, 4, 6, 8

```

#### Conditional List Comprehension

```py
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

```

### Using List Comprehension to refactor our 50 States code from Section 25

- _See Sec26.V198_

- In particular refactor this section:

```py
#these four lines of code
missing_states = []
for state in all_states:
    if state not in guessed_states:
        missing_states.append(state)

# become:
missing_states = [state for state in all_states if state not in guessed_states]


```

### Dictionary Comphrension

#### From a List

- _Dictionary Comprehension_ FROM a LIST

```py
#Names List
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# FORMAT:
# student_scores = {new_key:new_value for student in LIST}
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)


```

#### From another Dictionary - use DICTIONARY.items()

- _Dictionary Comprehension_ FROM a **another** Dictionary

```py
#using student_scores dictionary from above

# passed_students = {new_key:new_value for (key, value) in DICTIONARY.items()}
# passed_students = {new_key:new_value for (key, value) in DICTIONARY.items() if test}
passed_students = {student:score for (student, score) in student_scores.items() if score > 50}

print(passed_students)

```

### Iterate Over Pandas DataFrame

- Iterating over Pandas DataFrame PRETTY MUCH the same as Python Dict

```py
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

# Create new DataFrame from our student_dict
student_data_frame = pandas.DataFrame(student_dict)

#Loop through a data frame the ole fashion way = MESSY
# loops through names of columns and then data,
for (key, value) in student_data_frame.items():
    print(value)

```

#### Pandas DataFrame IN BUILT LOOP WITH == .iterrows() instead of .items()

- _See Sec 26. V.200_
- Each row is a Pandas Series Object, so we can access info with dot notation
- - such as search row for value `if row.student == "Angela": `

```py

                               '''    .iterrows() instead of .items()  '''
for (index, row) in student_data_frame.iterrows():
    print(index) #prints DataFrame, then each index number

    print(row) #prints out each row, bit sloppy tho

    '''Each row is a Pandas Series Object, so we can access info with dot notation'''
    print(row.student) #prints out DataFrame, then each student value (Angela, James Lilly)

    print(row.score) #same for the score values

    '''Use Conditional logic to only print Angela's Score'''
    if row.student == "Angela":
        print(row.score)

```

x

---

# 27. tkinter, \*args, \*\*kwargs, Creating GUI

- Sec 27.V206 - Keyword Arguments
- Order doesn't matter

```python
def my_function(a, b, c):
    #do this with a
    #that with b
    #finally this with c

my_function(C=3, a=1, b=2)

```

### Arguments with Default Values

- Specify the default values in the function

```python
def my_function(a=1, b=2, c=3):
    #do this with a
    #that with b
    #finally this with c

# my_function(C=3, a=1, b=2)
# call w/o params
my_function()

# To customize a value, specify in pararms
my_function(b=5)

'''Example using the Turtle library with font param in .write() function'''
import turtle

tim = turtle.Turtle()
tim.write("Some Text", font=("Times New Roman", 80, "bold"))

```

### Unlimited Arguments with single askterisk `*` (_args_)

- Sec 27. V.207.

- `*args` stands for arguments
- The asterisks is the key.
- - Single asterisk returns a tuple with the values passed in
- - could call it whatever you want, but stick with convention
- - Must include \* tho.
- format:

```py
# *args creates a tuple of your input, so here (3, 5, 6)
def add(*args):
    for n in args:
        print(n)

```

### Unlimited Keyword Arguments with double askterisks `**` (_kwargs_)

- Sec 27. V.208.

- `**kwargs` stands for key word arguments
- The double asterisks is the key.
- - Double asterisk returns a dictionary of key, value pairs
- format:

```py

# Double askteriks ** "kwargs" (keyword arguments)
# pass in n, the normal positional argument
def kwargs_calculate(n, **kwargs):
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

```

#### Use .get() to make \*\*kwargs optional:

```py

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

```

- x

- Using tkinter Button, Label and Entry Classes:

-- x

---

# 31. Flash Card Project

- Start in Section 31. V.234.

## Pandas DataFrame.to_dict parameters

<img src="https://i.imgur.com/5t03nSQ.png" alt="Pandas" width="100">

![Pandas DataFrame.to_dict paramters](https://i.imgur.com/5t03nSQ.png)

- Sec 31. Vid 242. around (4:30) see **Try, Except and Else** block:

```py
'''READ from our updated CSV list of remaining words to learn (Sec 31 V242 (4:30))'''
to_learn = {}
try:
  data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
  # data = pandas.read_csv("data/french_words.csv") #dataframe
  original_data = pandas.read_csv("data/french_words.csv")
  to_learn = original_data.to_dict(orient="records")
else:
  to_learn = data.to_dict(orient="records")

```

### index=False param to avoid increasing index columns on each .to_csv() save

```py

#Add is_known new function is_known in Sec 31 Video 242 (00:55)
def is_known():
  to_learn.remove(current_card) #remove current card from to_learn dictionary
  print(len(to_learn))
  '''Use Pandas to create a NEW dataframe to store remaining words to learn (Sec 31 V242 (3:10))'''
  data = pandas.DataFrame(to_learn)
  # data.to_csv("data/words_to_learn.csv") #overwrites the csv file every time to_learn dictionary is udpated
  '''Sec 31, Vid 242 (8:05) set index to False to avoid increasing index columns on each save'''
  data.to_csv("data/words_to_learn.csv", index=False)

  next_card()

```

---

### Note on git merge

- _Fell behind current state and tried to push up changes. (2/8/25)_
- Followed these commands from [freecodecamp article](https://www.freecodecamp.org/news/git-pull-force-how-to-overwrite-local-changes-with-git/)

1. `git fetch`
2. `git reset --hard HEAD`
3. `git merge origin`
   - this returned error message, and then followed conflict manager in VS code
