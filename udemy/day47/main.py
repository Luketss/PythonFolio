import requests

from bs4 import BeautifulSoup

class Ebay_Price_Picker:
    def __init__(self, item_url, preco_ideal):
        self.item_url = item_url
        self.preco_ideal = preco_ideal

    def get_ebay_price(self):
        headers = {"Content-Type": "application/json","User-Agent": "*"}
        r = requests.get(self.item_url, headers)
        
        soup = BeautifulSoup(r.text, "html.parser")
        price = soup.find('span', class_='notranslate').text

        return price

if __name__ == '__main__':
    a = Ebay_Price_Picker(item_url='https://www.ebay.com/itm/393419045168?hash=item5b999a3930:g:CdwAAOSwTcxg3Hsc&var=662251677098', preco_ideal=100)
    price = a.get_ebay_price()
