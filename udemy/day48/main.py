import os
import time
import requests
import shutil
import threading

from selenium import webdriver



def get_gecko():
    url = 'https://github.com/mozilla/geckodriver/releases/latest'
    r = requests.get(url, allow_redirects=True)

def is_gecko_in_folder():
    if os.path.isdir('./driver'):
        return True
    os.mkdir('./driver')
    return ('folder created')

class Cookie:
    def __init__(self):
        self.browser = self.selenium_cookie()

    def selenium_cookie(self):
        browser = webdriver.Firefox(executable_path=r'C:\\geckodriver.exe')
        browser.get('https://games-online.io/game/cake-maker/')
        time.sleep(7)

        return browser

    def click_cookie(self):
        self.browser.find_element_by_xpath("//*[@id='bigCookie']").click()

    def get_current_cookie_count(self):
        return self.browser.find_element_by_id("cookies").text

    def save_game(self):
        self.browser.find_element_by_xpath("//*[@id='prefsButton']").click()

if __name__ == '__main__':
    # print(is_gecko_in_folder())
    cook = Cookie()
    while True:
        cook.click_cookie()
