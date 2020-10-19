class Ponto:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_ponto(self):
        return(self.__x, self.__y)

class Retangulo:

    def __init__(self, largura, altura):
        self.__largura = largura
        self.__altura = altura

    def centro_retangulo(self):
        centro = (self.__altura * self.__largura) / 2
        return centro

def main():

    ponto1 = Ponto(2, 3)

    retangulo1 = Retangulo(4, 6)

    print(retangulo1.centro_retangulo())

    print(ponto1.get_ponto())
    a, b = ponto1.get_ponto()

    print(a, b)

main()
