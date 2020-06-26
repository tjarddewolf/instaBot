"""
Created by Tjard de Wolf
Date : 25/6/2020
 """

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import password #contains email and password

class InstagramBot():
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

        # sleep required for ReactJS loading
        time.sleep(2)

        emailInput = self.browser.find_element_by_name("username")
        passwordInput = self.browser.find_element_by_name("password")

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)

        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def dealWithPopups(self):
        # Deal with button location (answer = not now)
        button_location = self.browser.find_element_by_xpath('//button[text()="Niet nu"]')
        button_location.click()

        time.sleep(1)
        #Deal with button notifications (answer = not now)
        button_notifications = self.browser.find_element_by_xpath('//button[text()="Niet nu"]')
        button_notifications.click()


    def followAll(self):
        #go to 'alle weergaven'
        link_display = self.browser.find_element_by_xpath("//*[contains(text(), 'Alles weergeven')]")
        link_display.click()
        time.sleep(2)

        #get first button with follow and click on it.
        for i in range(1,follow_amount):
            #try because of ReactJS
            try:
                buttons_follow = self.browser.find_element_by_xpath("//button[text()='Volgen']")
                buttons_follow.click()
                self.browser.execute_script("window.scrollTo(0, 1080*i/50)")
                time.sleep(1)
                #Second try because of Instagram pop ups
                try:
                    link_display = self.browser.find_element_by_xpath("//*[contains(text(), 'OK')]")
                    link_display.click()
                except:
                    print('The code has been halted by Instagram')
            except:
                print('Going to next iteration: ', i)
            time.sleep(5)

    def closeBrowser(self):
        self.browser.close()

# ------------
"""Parameters:"""
#set email and password from password.py
email = password.email
password = password.password

#Set amount of follows to do
#( 0 = nobody will be followed, 50 = 50 people will be followed)
follow_amount = 45

#instantiate bot
test = InstagramBot(email = email,
                    password = password)

test.signIn()
test.dealWithPopups()
test.followAll()
test.closeBrowser()

