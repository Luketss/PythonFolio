class Conta:
    def __init__(self, numero, nome, saldo, limite=1000.0):
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)
    
    def exibir_saldo(self):
        return self.__saldo

def main():

    conta = Conta(1, "Lucas", 50.0)
    conta2 = Conta(2, "Sofia", 100.0, 2000.0)

    saldo = conta.exibir_saldo()
    print('Saldo atual do Lucas ' + str(saldo))

    saldo = conta2.exibir_saldo()
    print('Saldo atual da Sofia ' + str(saldo))
    print('realizando transferencia...')
    conta.transferir(conta2, 30.0)

    saldo = conta.exibir_saldo()
    print('Saldo atual do Lucas ' + str(saldo))

    saldo = conta2.exibir_saldo()
    print('Saldo atual da Sofia ' + str(saldo))


if __name__ == "__main__":
    main()
