class Bola():

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor

if __name__ == "__main__":
    couro = Bola("Azul", 15, "Couro")
    plastico = Bola("Marrom", 50, "plastico")
    print("A bola tem a cor: " + couro.cor + "\n E o material é de: " + couro.material )
    couro.trocaCor("Vermelho")
    print("Nova cor da bola: " + couro.cor)
    cor = plastico.mostraCor()
    print(cor)

