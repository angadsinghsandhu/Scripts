from selenium import webdriver
from time import sleep

#define a file with real username,password
from password_tind import username,password

class Tinderbot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://t.com')

        sleep(2)

        fb_btn = self.driver.find()
        fb_btn.click()

        #see for new window
        base_window = self.driver.window_handles[0]
        pop_up_window = self.driver.window_handles[1]

        #switching to pop-up window
        self.driver.switch_to_window(pop_up_window)

        #typing email
        email_in = self.driver.find_element_by_xpath('')
        email_in.send_keys(username)

        #typing password
        password = self.driver.find_element_by_xpath('')
        password.send_keys(password)

        #clicking in the login button
        login_btn = self.driver.find_element_by_xpath('')
        login_btn.click()

        #switching back to orignal window
        self.driver.switch_to_window(base_window)

        #handling pop-ups
        popup_1 = self.driver.find_element_by_xpath()
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath()
        popup_2.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath()
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath()
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match_popup()


    def close_popup():
        popup_3 = self.driver.find_element_by_xpath()
        popup_3.click()

    def close_match_popup():
        match_popup = self.driver.find_element_by_xpath()
        match_popup.click()

#DRIVER Code
#bot = Tinderbot()
#bot.login()
