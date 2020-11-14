from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyotp

#VARIABLE
USERNAME = '' #PUT YOUR USERNAME HERE
PASSWORD = '' #PUT YOUR PASSWORD HERE
SECRETKEY = '' #PUT YOUR SECRET KEY HERE
DRIVERFILE = '' #PUT YOUR CHROMEDRIVER PATH HERE

def otp():
    totp = pyotp.TOTP(SECRETKEY)#YOUR 2FA SECRET KEY
    return totp.now()

def main():
    while True:

        driver = webdriver.Chrome(DRIVERFILE)
        driver.get('https://freebitco.in/?op=signup_page')
        login = driver.find_element_by_class_name('login_menu_button')
        login.click()
        sleep(1)
        user = driver.find_element_by_id('login_form_btc_address')
        user.send_keys(USERNAME)#YOUR USERNAME
        password = driver.find_element_by_id('login_form_password')
        password.send_keys(PASSWORD)#YOUR PASSWORD
        autha = driver.find_element_by_id('login_form_2fa').send_keys(otp())
        sleep(3)
        allow = driver.find_element_by_class_name('pushpad_deny_button').click()
        button.click()
        sleep(4)
        nocaptcha = driver.find_element_by_xpath('//div[@class="play_without_captcha_button center"][@id="play_without_captchas_button"]').click()
        sleep(1)
        roll = driver.find_element_by_id('free_play_form_button').click()
        sleep(4)
        driver.close()
        sleep(3650)
main()
