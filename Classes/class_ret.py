class Ret:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def change_side_value(self, new_base, new_altura):
        """
        altera o valor da base e da altura
        """
        self.base = new_base
        self.altura = new_altura

    def devorve_lados_value(self):
        """
        retorna os valores da base e altura
        """
        return(self.altura, self.base)

    def calculate_area(self):
        """
        base * altura
        """
        area = self.base * self.altura
        return area

if __name__ == "__main__":
    obj1 = Ret(5, 7)

    obj2 = Ret(2, 2)

    obj3 = Ret(3, 4)

    a, b = obj1.devorve_lados_value()
    print("O valor da base é: " + str(b) + "\n O valor da altura é: " + str(a))
    
    aresa = obj3.calculate_area()
    print("O valor da area é de: " + str(aresa))
