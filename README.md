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

----
6. choice() with import random

```python

import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
card = random.choice(cards)

```

---
7.  Use _ in loop instead of rando variable: 

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

11. 