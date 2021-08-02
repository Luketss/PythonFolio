import os
import time
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Net:
    def __init__(self):
        self.browser = self.selenium_get_browser()

    def selenium_get_browser(self):
        #not recomended to use this path, instead, create a function to download and save the right path
        browser = webdriver.Firefox(executable_path=r'C:\\geckodriver.exe')
        browser.get('https://www.speedtest.net/')
        time.sleep(1)

        return browser
    
    def start_internet_test(self):
        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='start-text']"))
        ).click()


    def find_internet_speed(self):
        speed = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='result-data-large number result-data-value download-speed']")
            )
        )
        return speed.text


    def find_upload_speed(self):
        upload = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='result-data-large number result-data-value upload-speed']")
            )
        )
        return upload.text

if __name__ == '__main__':
    
    internet = Net()
    internet.start_internet_test()
    time.sleep(60)
    speed, upload = internet.find_internet_speed(), internet.find_upload_speed()