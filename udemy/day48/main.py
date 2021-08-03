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
        return self.browser.find_element_by_id("FileLoadInput").click()

    def load_game(self):
        self.browser.find_element_by_xpath("//*[@id='prefsButton']").click()

    def get_unloked_items(self):
        a = self.browser.find_element_by_id("products")
        children = a.find_elements_by_xpath("//div[@class='price']")
        for value in children:
            print(value.text)
        #self.click_unlocked_item(children) 

    def click_unlocked_item(self, children):
        pass

if __name__ == '__main__':
    timeout = time.time() + 5
    # print(is_gecko_in_folder())
    cook = Cookie()
    while True:
        cook.click_cookie()

        # if time.time() > timeout:
        #     print(cook.get_unloked_items())

        #     timeout = time.time() + 5

#<a class="option" style="position:relative;"><input id="FileLoadInput" type="file" style="cursor:pointer;opacity:0;position:absolute;left:0px;top:0px;width:100%;height:100%;" onchange="Game.FileLoad(event);" onclick="PlaySound('snd/tick.mp3');">Load from file</a>