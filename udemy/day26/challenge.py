new_list = [num * 2 for num in range(1,5)]

names = ['Alex', 'Beth', 'Dave', 'Eleanor', 'Freddie']

short_names = [name for name in names if len(name) < 5]

long_names = [name.upper() for name in names if len(name) > 4]
print(short_names)

