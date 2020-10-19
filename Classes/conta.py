class Conta(object):

    def __init__(self, num_conta, nome_correntista):
        self.__num_conta = num_conta
        self.__nome_correntista = nome_correntista
        self.__saldo = 0

    def alterar_nome(self, new_name):

        if self._is_new_name_valid(new_name):
            self.name = new_name
    
    def _is_new_name_valid(self, new_name):
        if not isinstance(new_name, str):
            return False
        return True

    def deposito(self, valor_deposito):
        if self._is_valueofentry_valid(valor_deposito):
            self.__saldo += valor_deposito

    def get_saldo(self):
        return self.__saldo

    def saque(self, saque):
        if self._is_valueofentry_valid(saque):
            self.__saldo -= saque
    
    def _is_valueofentry_valid(self, valor_deposito):
        if not isinstance(valor_deposito, float):
            return False
        return True
    
class Conta_Poupanca():

    def __init__(self, Conta):
        super().__init__(Conta)

    def render(self):
        saldo = self.get_saldo()
        saldo += 2
        self.Conta.deposito(saldo)




if __name__ == "__main__":
    conta1 = Conta_Poupanca(1, "Lucas Costa")

    conta1.deposito(150.00)
    print(conta1.get_saldo())
    conta1.render()   
    print(conta1.get_saldo())
    conta1.saque(40.00)
    print(conta1.get_saldo())
