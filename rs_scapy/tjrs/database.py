import sqlite3
from sqlite3 import Error

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.http import Request
from scrapy.pipelines.files import FilesPipeline

class SQLDatabasePipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        self.connection = self.create_connection()
        self.cursor = self.connection.cursor()

    
    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect('banco.db')
            return conn
        except Error as e:
            print(e)

    def check_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS data (
            tipo TEXT,
            numero TEXT,
            data_apresentacao TEXT,
            processo_administrativo TEXT,
            valor TEXT,
            origem TEXT,
            pagador TEXT,
            advogados TEXT,
            objeto TEXT,
            orcamento TEXT,
            situacao TEXT,
            localizacao TEXT,
            tribunal TEXT,
            posicao TEXT
        )'''
        self.cursor.execute(query)


    def process_item(self, item, spider):
            """
            Save quotes in the database
            This method is called for every item pipeline component
            """
            self.check_table()
            adapter = ItemAdapter(item)
            tup = (dado for dado in adapter['dados'])
            query = 'INSERT INTO data (tipo,numero,data_apresentacao,processo_administrativo,valor,origem,pagador,advogados,objeto,orcamento,situacao,localizacao,tribunal,posicao) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
            self.cursor.execute(query,(adapter['dados'][0],adapter['dados'][1],adapter['dados'][2],adapter['dados'][3],adapter['dados'][4],adapter['dados'][5],
            adapter['dados'][6],adapter['dados'][7],adapter['dados'][8],adapter['dados'][9],adapter['dados'][10],adapter['dados'][11],
            adapter['dados'][12],adapter['dados'][13]
            )
            )
            self.connection.commit()

            return item