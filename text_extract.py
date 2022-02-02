'''
buscar dentro da listagem os processos que tenham na mesma página o cancelamento e requisitorio.
Em seguida, dentro do texto da página, buscar também o número do processo com um look ahead
'''
import re

from io import StringIO
from bs4 import BeautifulSoup
from tika import parser
from os import listdir
from os.path import isfile, join

a = '5021497-35.2019.4.04.9388'

proc = f'{a}'.replace('-', '.')
proc_li = f'{proc}'.replace('.', '')

patterns_ahead = [
    r'(cancelamento).*?(requisitório).*?(?<=' + proc + ')',
    r'(cancelamento).*?(requisitório).*?(?<=' + proc_li + ')',
    r'(cancelamento).*?(precatório).*?(?<=' + proc + ')',
    r'(cancelamento).*?(precatório).*?(?<=' + proc_li + ')',
    r'(cancelado).*?(precatório).*?(?<=' + proc + ')',
    r'(cancelado).*?(precatório).*?(?<=' + proc_li + ')',
    r'(cancelar).*?(precatório).*?(?<=' + proc + ')',
    r'(cancelar).*?(precatório).*?(?<=' + proc_li + ')'
]

patterns = [
    r'(cancelamento).*?(requisitório)',
    r'(cancelamento).*?(precatório)',
    r'(cancelado).*?(precatório)',
    r'(cancelar).*?(precatório)'
]

eliminad = False

def ParsePDFContent(file_path: str) -> BeautifulSoup:
    parsed_data = parser.from_file(file_path, xmlContent=True)
    parsed_full_data = parsed_data['content']
    return BeautifulSoup(parsed_data['content'], features='lxml')

def FormatData(content: str) -> str:
    #Remove html tags
    text = re.sub(r'<.*>', '', content)
    #remove todas quebras de linha, transformando o texto em 1 unica linha
    text = re.sub(r'\n{1,15}', ' ', text)
    return text

def FindFilenames(path_to_dir: str) -> list:
    return [ filename for filename in listdir(path_to_dir) if isfile(join(path_to_dir, filename)) ]

def CheckOk(isFind, p='-', text='-', page='-', file='-'):
    with open('result.txt', 'a') as file_txt:
        file_txt.write(f'{isFind}, \n {p}, \n {text}, \n {page}, \n {file}\n')

def CheckPatt(file, text):
    for p in patterns:
        m = re.search(p, text, flags=re.IGNORECASE)
        if m is not None:
            print('Eliminado', p, page+1, file)
            # CheckOk('Eliminado', p, m.group(), page+1, file)
            # eliminad = True

def CheckOPatt(file, text):
    for p in patterns_ahead:
        m = re.search(p, text, flags=re.IGNORECASE)
        if m is not None:
            print('Pattern Match', p, page+1, file)
            # CheckOk()
            # eliminad = True


if __name__ == '__main__':
    file_list = FindFilenames(f'./Downloads/{a}')
    for file in file_list:
        xhtml_data = ParsePDFContent(f'./Downloads/{a}/{file}')
        for page, content in enumerate(xhtml_data.find_all('div', attrs={'class': 'page'})):
            text = FormatData(str(content))
            CheckPatt(file, text)
            # CheckOPatt(file, text)
    # if eliminad == False:
    #     CheckOk('Não Encontrado')