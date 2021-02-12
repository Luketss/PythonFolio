'''sobreMim = 'Meu nome é Lucas e minha idade 22'

meuNome = 'Lucas'

substring = meuNome[2:5]
substring2 = meuNome[:5]
substring3 = meuNome[2:]
print(substring)'''

'''url = 'https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500'
index = url.find('=')
# a função find() retorna o indice do caractere buscado dentro da string
substring = url[index + 1:]
print(substring)

argumento = 'moedaorigem=real'
#
listaArgumento = argumento.split('=')
print(listaArgumento)'''

class Extrator_Argumentos_Url:
    def __init__(self, url):
        if self.url_E_Valida(url):
            self.url = url
        else:
            raise LookupError("Url Inválida")

    @staticmethod
    def url_E_Valida(url):
        if url:
            return True
        else:
            return False
    
    def extrai_Argumentos(self):

        busca_moeda_origem = 'moedaorigem'
        busca_moeda_destino = 'moedadestino'

        indice_inicial_moeda_destino = self.encontra_indice_inicial(busca_moeda_destino)

        indice_inicial_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
        indice_final_moeda_origem = self.url.find("&")

        moeda_origem = self.url[indice_inicial_moeda_origem : indice_final_moeda_origem]
        moeda_destino = self.url[indice_inicial_moeda_destino:]

        '''indice_inicial_moeda_destino = self.url.find('=', 15)

        indice_final_moeda_origem = self.url.find('=')
        indice_inicial_moeda_origem = self.url.find('&')

        moeda_origem = self.url[indice_final_moeda_origem + 1:indice_inicial_moeda_origem]
        moeda_destino = self.url[indice_inicial_moeda_destino + 1:]'''

        return moeda_origem, moeda_destino

    def encontra_indice_inicial(self, moeda_buscada):
        return self.url.find(moeda_buscada) + len(moeda_buscada) + 1

def main():
    url = 'moedaorigem=real&moedadestino=dolar'

    obj1 = Extrator_Argumentos_Url(url)

    moeda_origem, moeda_destino = obj1.extrai_Argumentos()

    print(moeda_origem + ' & ' + moeda_destino)
if __name__ == "__main__":
    main()