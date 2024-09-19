#if / else

#Good Visualization Tool: https://pythontutor.com/visualize.html#mode=edit

#name = 'Alice'
#if name == 'Alice':
#    print('Hello, Alice')
#print('Done')

import random
import time

def displayIntro():
    print('dragon game text went here')

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? Select 1 or 2')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('A large dragon jumps in front of you')
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('You slayed the dragon and got the treasure!')
    else:
        print('Dragon ate your ass!')


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again - Select yes or no')
    playAgain = input()
    
