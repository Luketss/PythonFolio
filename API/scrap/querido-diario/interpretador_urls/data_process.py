#import magic
from tika import parser
import urllib.request
import wget
import requests


class Pdf_data_reader:
    def __init__(self, gazzete_file_path):
        self.gazzete_file_path = gazzete_file_path

    def request_pdf_content(self):
        header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
        }
        try:
            r = requests.get(self.gazzete_file_path, headers=header)
            with open('teste.txt', 'w', encoding='utf-8') as f:
                f.write(r.text)
                file_data = parser.from_file('teste.txt')
                text = file_data['content']
                print(text)

        except ValueError as e:
            print('error on urllib ' + str(e))

    
    def get_row(self):
        return self.gazzete_file_path
