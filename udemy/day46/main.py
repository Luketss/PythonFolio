import requests
from datetime import date

class Bilboards:
    def __init__(self, link, data=date.today()):
        self.link = f'{link}/{data}'

    
    def get_billboard(self):
        r = requests.get(self.link)
        
        with open('result.txt', 'w') as f?
            f.write(r.text)

        return r.text



if __name__ == '__main__':
    top_musics = Bilboards('https://www.billboard.com/charts/hot-100')

    print(top_musics.get_billboard())