import os
import re
import json
import requests

from bs4 import BeautifulSoup
from datetime import date

TOKEN_SP = "BQA4sBVuGHTqeu4JB2D-kJv6vw19vsQdAcQty63ZN-lUkjyLPDWM_tl54rNh_tYRXzetqWdmaXmhTgZuUyyPTo6nDwKnM0tBdjycJofWQT-zGpQf6nhUwK5xHeBUf_ss1CwoDMLjIroFqDFQa7-DfdzB4na3Qq1Y1SFqZv7YGxL_ZLaT8OIeBqZC1GHYxdPL6S9QlZLqnD6zbhrFwZ6EW0U1hhExq12kD4IKpWCkSBKA4e2yNgv8UT1bSpjh-SjIib6bYCxkeCOx92WrUn6N"

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

    def get_top_musics_from_html(self) -> str:
        uri = []
        try:
            soup = BeautifulSoup(self._html, features='html.parser')

            music_title = soup.find_all(name="span", class_="chart-element__information__song", text=True)

            with open('top100.txt', 'w', encoding='utf-8') as f:
                for (index, name) in enumerate(music_title):
                    print(f'Buscando uri da {name}')
                    uri.append(self.search_for_music(re.sub('</*span.*?>', '', str(name))))
                    
            for (index, value) in enumerate(uri):
                print(index, value)
        except ValueError as e:
            print(f'Error on get_top_musics_from_html: {e}')

    def search_for_music(self, name_music):
        url = 'https://api.spotify.com/v1/search?'
        track = 'track'
        query = f'{url}q={name_music}&type={track}&market=US&limit=5&offset=5'

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TOKEN_SP}",
        }

        response = requests.get(query, headers=headers)
        response_json = response.json()

        uri = self.get_response_uri(response_json)

        return uri

    def get_response_uri(self, json_response):
        return json_response['tracks']['items'][0]['uri']


if __name__ == '__main__':
    bilboard_obj = Bilboards('https://www.billboard.com/charts/hot-100')
    html_content = bilboard_obj.get_billboard()

    top_music = Top_musics(html_content)
    top_music.get_top_musics_from_html()

    