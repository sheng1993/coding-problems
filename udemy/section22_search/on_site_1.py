# Given a dice which rolls 1 to 7, simulate a 5 sided dice.
# Preferably, write your solution as a function

from random import randint

def dice7():
    return randint(1,7)

def convert7to5():
    roll = 7

    while roll > 5:
        roll = dice7()
    
    return roll