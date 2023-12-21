from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self, username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_encoded_extension('prefs',{'intl.accept_languages': 'en,en_US'})
        self.browser= webdriver.Chrome('chromedriver.exe',chrome_options=self.browserProfile)
        self.username = username
        self.password = password

        def signIn(self):
            self.browser.get("https://twitter.com/i/flow/login")
            time.sleep(3)

            usernameInput= self.browser.find_element_by_xpath("")