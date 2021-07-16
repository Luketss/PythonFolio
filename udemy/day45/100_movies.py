import requests
from bs4 import BeautifulSoup

def main():
    r = requests.get('https://www.imdb.com/list/ls000041191/')
    soup = BeautifulSoup(r.text, features='html.parser')

    film_titles = soup.find_all("img", {"class": "loadlate"})

    with open('request.txt', 'w') as file:
        for (index, value) in enumerate(film_titles):
            file.write(f"{index} {value['alt']} \n")

if __name__ == '__main__':
    main()