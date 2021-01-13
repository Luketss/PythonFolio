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

    def __str__(self):
        return (f'{self._nome} - {self.ano} - {self._like} Likes')
    
    # def imprime(self):
    #     print(f'{self._nome} - {self.ano} - {self._like} Likes')
    
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    def __str__(self):
        return (f'{self._nome} - {self.ano} - {self.duracao} min - {self._like} Likes')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return (f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._like} Likes')
   
    
def main():
    vingadores = Filme('Vingadores', 2018, 160)
    atlanta = Serie('Atlanta', 2018, 3)

    vingadores.dar_like()

    print(vingadores.get_likes())
    vingadores.nome = 'Vingadores - Guerra infinita'
    print(vingadores.nome)

    filmes_series = [vingadores, atlanta]

    for programa in filmes_series:
        print(programa)

    

    # for programa in filmes_series:
    #     detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    #     print(f'O nome é: {programa.nome} - {detalhes}')

if __name__ == '__main__':
    main()