import requests
from bs4 import BeautifulSoup

class Request:
    def __init__(self, date):
        self.url = 'https://www.billboard.com/charts/hot-100/' + date

    def get_billboard_information(self) -> str:
        """get billboard.com data

        Returns:
            str: html content
        """
        r = requests.get(self.url)
        with open('result.txt', 'w', encoding='utf-8') as f:
            f.write(r.text)
        return r.text

    def parse_html(self, html_text):
        soup = BeautifulSoup(html_text, features='html.parser')

    def main(self):
        self.parse_html(self.get_billboard_information())


if __name__ == '__main__':
    make = Request('1974-01-12')
    make.main()
