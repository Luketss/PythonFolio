from sys import exit
import random


def calculate_futuros_probability():
    selected_numbers = []
    probability_sum = 0

    for value in range(0,6):
        number = random.randint(1,20)
        selected_numbers.append(number)
        probability_sum = probability_sum + number
    return probability_sum

def bankrupt(reason):
    print reason, "It's over!"
    exit(0)

def contratos_futuros_room():
    print "You see the walls and know nothing, but you give it a shot"

    next = raw_input("> ")

    if next == "ind":
        print "OH, good choise!"
        ind()
    elif next == "dol":
        print "Ok, go on!"
        dol()
    else:
        bankrupt("")

def start():
    print "You are now on the stock game!"
    print "Here you will know what kind of profile do you have."
    print "Choose your path right now!!! (left - right - center)"

    next = raw_input("> ")

    if next == "left":
        contratos_futuros_room()
    elif next == "center":
        renda_fixa_room()
    elif next == "right":
        bovespa_room()
    else:
        bankrupt()
