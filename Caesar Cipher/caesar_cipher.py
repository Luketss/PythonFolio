

def main():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    text = input('Insira sua palavra')
    shift = input('Shift text value')
    result = ''

    for letter in text:
        result += chr(ord(letter) + int(shift))
    print(result)


if __name__ == '__main__':
    main()
