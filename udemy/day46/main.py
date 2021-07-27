import requests

from bs4 import BeautifulSoup
from datetime import date

class Bilboards:
    def __init__(self, link, data=date.today()):
        self.link = f'{link}/{data}'

    
    def get_billboard(self):
        try:
            r = requests.get(self.link)
            self.write_file(r.text)

            return r.text
        except ValueError as e:
            print(f'Error on get_billboard: {e}')

    def write_file(self, text):
        try:
            with open('result.txt', 'w', encoding='utf-8') as f:
                    f.write(text)
        except ValueError as e:
            print(f'Error on write_file: {e}')

class Top_musics:
    def __init__(self, html):
        self._html = html

    def tag_visible(self, element):
        if element.parent.name in ['span']:
            return True
        return False


    def get_top_musics_from_html(self) -> str:

        try:
            soup = BeautifulSoup(self._html, features='html.parser')

            music_title = soup.findAll(name="span", class_="chart-element__information__song")
            visible_texts = filter(self.tag_visible, music_title)

            with open('top100.txt', 'w', encoding='utf-8') as f:
                for (index, value) in enumerate(music_title):
                    f.write(f"{index}) {value} \n")
        except ValueError as e:
            print(f'Error on get_top_musics_from_html: {e}')



if __name__ == '__main__':
    bilboard_obj = Bilboards('https://www.billboard.com/charts/hot-100')
    html_content = bilboard_obj.get_billboard()

    top_music = Top_musics(html_content)
    top_music.get_top_musics_from_html()
