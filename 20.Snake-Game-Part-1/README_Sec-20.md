# Time Module


```py
import time 

# while game is running
game_is_on = True
while game_is_on:
    '''Using time module, add a 1 second delay (Sec 20. V.148 (6:40))'''
    time.sleep(0.1) #one-tenth second delay after all three segments have moved (faster)

```


# For in Range - from C Language

- Can't use these keywords, but helpful in remembering the positional arguments
- `for seg_num in range(start= len(segments) - 1, stop= 0, step= -1):`

```py

    ''' range comes from C Language (not pure python) Can't use keywords start, stop, step '''
    # for seg_num in range(start= 2, stop= 0, step= -1):
    # for seg_num in range(start= len(segments) - 1, stop= 0, step= -1):
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    #outside for loop, grap the first segment and move it forward 20 paces
    segments[0].forward(20)
    # segments[0].left(90) #continuous circle

```



# Sec 20 - V149 - Refactor Using Classes

- x