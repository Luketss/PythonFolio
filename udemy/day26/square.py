nums_to_class = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers


    def square(self):

        square_numbers = [num ** 2 for num in numbers]

        print(square_numbers)


    def even(self):
        even_numbers = [num for num in numbers if num % 2 == 0]
        print(even_numbers)

    def common(self):
        l1 = []
        l2 = []
        result = []

        l1 = self.read_file('file1.txt')
        l2 = self.read_file('file2.txt')

        for value in l1:
            for num in l2:
                if value == num:
                    result.append(num)
        return result

    def read_file(self, path_to_file):
        value_list = []
        with open(path_to_file) as f:
            content = [value_list.append(int(num)) for num in f.readlines() if num not in value_list]
        return value_list


if __name__ == '__main__':
    num = Numbers(nums_to_class)
    iguais = num.common()
    print(sorted(iguais))
