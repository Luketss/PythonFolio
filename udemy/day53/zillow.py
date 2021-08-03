import typing
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Zillow:
    def __init__(self) -> None:
        self.browser = self.start_selenium()

    def start_selenium(self):
        browser = webdriver.Firefox(executable_path=r'C:\\geckodriver.exe')
        browser.get('https://www.zillow.com/')
        return browser

    def go_to_search_page(self):
        WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Rent']"))
        ).click()

    def get_zillow_rental_list(self):
        try:
            WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="grid-search-results"]'))
            )

            time.sleep(2)
            rental_props = self.browser.find_elements_by_xpath('//ul[@class="photo-cards"]')
            for value in rental_props:
                print(value.text)

        except ValueError as e:
            print(f'get rental list error {e}')


    def extract_zillow_price(self):
        pass

if __name__ == '__main__':
    zillow_obj = Zillow()
    zillow_obj.go_to_search_page()
    zillow_obj.get_zillow_rental_list()