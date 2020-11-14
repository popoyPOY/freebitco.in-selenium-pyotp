from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyotp


def otp():
    totp = pyotp.TOTP('')#YOUR 2FA SECRET KEY
    return totp.now()

def main():
    while True:

        driver = webdriver.Chrome("D:/chromedriver.exe")
        driver.get('https://freebitco.in/?op=signup_page')
        login = driver.find_element_by_class_name('login_menu_button')
        login.click()
        sleep(1)
        user = driver.find_element_by_id('login_form_btc_address')
        user.send_keys('')#YOUR USERNAME
        password = driver.find_element_by_id('login_form_password')
        password.send_keys('')#YOUR PASSWORD
        button = driver.find_element_by_id('login_button')
        autha = driver.find_element_by_id('login_form_2fa').send_keys(otp())
        button.click()
        sleep(2)
        allow = driver.find_element_by_class_name('pushpad_deny_button').click()
        sleep(3)
        nocaptcha = driver.find_element_by_xpath('//*[@id="play_without_captchas_button"]').click()
        sleep(5)
        roll = driver.find_element_by_id('free_play_form_button').click()
        sleep(1)
        driver.close()
        sleep(3650)
main()
