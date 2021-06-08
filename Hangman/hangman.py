import random
from display import display_hangman

def check_entry_value(word, letter):
    if (letter in word):
        return True
    return False

def choose_word():
    word = [
    'repeat',
    'rear',
    'denial',
    'ambiguous',
    'summary',
    'option',
    ]

    return(random.choice(word))

def main():
    word = choose_word()
    word_visual = '_' * len(word)
    guessed = False
    letters = [letter for letter in word]
    tries = 6
    print(display_hangman(tries))

    while not guessed and tries > 0:
        print(word_visual)
        letter = input().lower()
        if (check_entry_value(word, letter)):
            print('tem')
        else:
            print('não tem')
            tries -=1
        print(word, tries)
        print(display_hangman(tries))

    if not guessed:
        print('lose')


if __name__ == '__main__':
    main()

