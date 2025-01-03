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

16. exitonclick() method from Turtle module

```py
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick() #program runs until user closes it.

```

---


17. 
