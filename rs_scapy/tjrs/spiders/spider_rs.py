import scrapy

import sqlite3
from sqlite3 import Error

from tjrs.items import TjrsItem

class TJRS(scrapy.Spider):
    name = "spider_tjrs"
    start_range = 60000
    final_range = 68000

    #ranges pesquisados 30000 até 37999, 58000 até 60000 e de 120000 até 208500
    def start_requests(self):
        for processo in range(self.start_range, self.final_range):
            url = f'https://www.tjrs.jus.br/site_php/precatorios/precatorio.php?Numero_Informado={processo}&tipo_pesquisa=por_precatorio&aba_opcao_consulta='
            yield scrapy.Request(url=url, callback=self.parse)


        # print(self.result)


    def parse(self, response):
        if not response.css("div[id='conteudo'] table:nth-child(1)"):
            return 
        resultado = []
        table_conteudo = response.css("div[id='conteudo'] table:nth-child(1)")

        for tr in table_conteudo.css('tr'):
            tipo = tr.css('td strong::text').get()
            valor = tr.css('td:nth-child(2)::text').get()
            # print(tipo.strip(), valor.strip())
            resultado.append(valor.strip())
        # print(resultado)

        yield TjrsItem(
            dados=resultado
        )
        

    # def extract(self, response):
    #     resultado = []
    #     table_conteudo = response.css("div[id='conteudo'] table:nth-child(1)")

    #     for tr in table_conteudo.css('tr'):
    #         tipo = tr.css('td strong::text').get()
    #         valor = tr.css('td:nth-child(2)::text').get()
    #         # print(tipo.strip(), valor.strip())
    #         resultado.append(valor.strip())
    #     print(resultado)
    #     yield TjrsItem(
    #         dados=[resultado]
    #     )


        #self.log(f'Saved file response.txt')
    
    # def close_spider(self):
    #     print(self.result)
