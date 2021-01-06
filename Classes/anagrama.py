def anagramas(palavra):
    if len(palavra) <= 1:
        return palavra
    else:
        tmp = []
        for value in anagramas(palavra[1:]):
            for i in range(len(palavra)):
                tmp.append(value[:i] + palavra[0:1] + value[i:])
        return tmp

print(anagramas('imagine'))
