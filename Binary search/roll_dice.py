#choose your dices and roollll! 

import random

def roll_dices(number_of_dices):
    dices  = 1
    while dices <= number_of_dices:
        result = random.randint(1,6)
        print result
        dices = dices + 1

roll_dices(2)

