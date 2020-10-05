class Square(object):

    def __init__(self, lado):
        self.lado = lado

    def change_side_value(self, nw_side):
        self.lado = nw_side

    def back_side_value(self):
        print("Valor do lado: " + str(self.lado)) 

    def area_calculate(self):
        area = self.lado ** 2
        return area

if __name__ == "__main__":
    obj1 = Square(10)
    obj2 = Square(2)
    obj3 = Square(5)

    obj1.back_side_value()
    obj1.change_side_value(7)
    obj1.back_side_value()

    obj2.back_side_value()
    
    a = obj3.area_calculate()
    print("A area é: " + str(a))

    b = obj2.area_calculate()
    print("A area é: " + str(b))

    c = obj1.area_calculate()
    print("A area é: " + str(c))

