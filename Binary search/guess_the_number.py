import random

def validate_number(your_guess, number_to_guess):
    while your_guess != number_to_guess:
        if your_guess < number_to_guess:
            print "guess is too low"
            your_guess = int(input("Digite um numero: "))
        elif your_guess > number_to_guess:
            print "guess is too high"
            your_guess = int(input("Digite um numero: "))
        else:
            print "You've done!"
            break

print "Vamos tentar adivinhar o numero que eu escolhi!"
print "O numero deve ser positivo, entre zero e cinco"

number_to_guess = random.randint(0, 5)
print number_to_guess
your_guess = int(input("Digite um numero: "))

validate_number(your_guess, number_to_guess)


    