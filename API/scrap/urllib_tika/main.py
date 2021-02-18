import urllib.request
from tika import parser

url = 'https://www.mairie-orly.fr/content/download/11449/88884/file/Menu+du+mois+de+janvier+2021.pdf'

urllib.request.urlretrieve(url, './a.pdf')

file_data = parser.from_file('./a.pdf')

text = file_data['content']
print(text)
