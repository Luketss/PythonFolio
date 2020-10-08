class Pessoa():

    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def envelhecer(self):
        
        if self.__idade < 21:
            self.__altura += 0.5

        self.__idade += 1
        return self.__idade


    def engordar(self, engordou_peso):
        
        self.__peso += engordou_peso
        return self.__peso


    def emagrecer(self, emagreceu_peso):
        
        self.__peso -= emagreceu_peso

    def crescer(self, diferenca_altura):
        
        self.__altura += diferenca_altura

    def get_nome(self):

        return self.__nome

if __name__ == "__main__":
    lucas = Pessoa("Lucas", 22, 80, 1.78)

    print(lucas.get_nome())

    print(lucas.envelhecer())
    print(lucas.engordar(10))