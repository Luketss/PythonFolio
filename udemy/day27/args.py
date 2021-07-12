def sum_n_values(*args):
    soma = sum(value for value in args)

    return soma

def calculate(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

calculate(arroz=100, miojo=2)
print(sum_n_values(1,5,9,6,58,7,2))