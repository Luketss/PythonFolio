class Programa:
    def __init__(self, titulo, avaliacao, tipo):
        self.titulo = titulo
        self.avaliacao = avaliacao
        self.tipo = tipo
 
        if self.tipo == 'serie':
            ep = input('Digite o numero de episodios ')
            self.tempo = self.Serie(ep)
        else:
            du = input('Digite o numero de duracao ')
            self.tempo = self.Filme(du)

    def get_serie_ep(self):
        if self.tipo == 'serie':
            return self.tempo.episodios
        else:
            return('tempo total de duracao: ' + self.tempo.duracao + ' minutos')

    class Serie:
        def __init__(self, episodios):
            self.episodios = episodios

    class Filme:
        def __init__(self, duracao):
            self.duracao = duracao



if __name__ == '__main__':
    prog = Programa(titulo='Amanhecer 2', avaliacao=3, tipo='filme')
    print(prog.get_serie_ep())