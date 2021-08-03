import os
import time
import re

from selenium import webdriver

class Cookie:
    def __init__(self):
        self.browser = self.selenium_cookie()

    def selenium_cookie(self):
        browser = webdriver.Firefox(executable_path=r'C:\\geckodriver.exe')
        browser.get('http://orteil.dashnet.org/experiments/cookie/')
        time.sleep(5)

        return browser

    def click_cookie(self):
        self.browser.find_element_by_id('cookie').click()

    def get_store_price(self):
        items = self.browser.find_elements_by_css_selector('#store b')
        items_price = [re.sub('\D', '', item.text) for item in items]
        return (items, items_price)

    def get_current_money(self):
        return re.sub('\D', '', self.browser.find_element_by_id('money').text)

#dudu comentou bem para criar um event handler ao inves do while true
if __name__ == '__main__':
    timeout = time.time() + 5

    cook = Cookie()
    while True:
        cook.click_cookie()

        if time.time() > timeout:
            items, store_price = cook.get_store_price()
            money = cook.get_current_money()
            timeout = time.time() + 5
