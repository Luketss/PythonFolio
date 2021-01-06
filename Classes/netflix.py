class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0
    
    def dar_like(self):
        self._like += 1
    
    def get_likes(self):
        return self._like
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if self._is_new_name_valid(nome):
            self._nome = nome
        else:
            return print('Nome inválido')
    
    def _is_new_name_valid(self, new_name):
        if not isinstance(new_name, str):
            return False
        return True
    
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas
   
    
def main():
    vingadores = Filme('Vingadores', 2018, 160)

    vingadores.dar_like()

    print(vingadores.get_likes())
    vingadores.nome = 'Vingadores - Guerra infinita'
    print(vingadores.nome)

if __name__ == '__main__':
    main()