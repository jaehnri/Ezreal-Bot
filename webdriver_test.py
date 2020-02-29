from selenium import webdriver
from time import sleep

class EzrealBot():
    def __init__(self):
        options = webdriver.ChromeOptions()

        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs",prefs)

        self.driver = webdriver.Chrome(options=options)

    def login(self):
        self.driver.get("https://facebook.com/pokes")

        fb_email = self.driver.find_element_by_xpath('//*[@id="email"]')
        fb_email.send_keys('****')

        fb_pwd = self.driver.find_element_by_xpath('//*[@id="pass"]')
        fb_pwd.send_keys('****')

        fb_login = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        fb_login.click()        

    def poke(self):

        buttons = self.driver.find_elements_by_link_text('Cutuque de volta')

        for button in buttons:
            button.click()
            sleep(0.5)

bot = EzrealBot()
bot.login()

while True:
    bot.poke()