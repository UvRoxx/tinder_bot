from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from time import sleep

LOGIN_ID = os.environ["MAIL"]
LOGIN_PASS = os.environ["PASS"]

URL = "https://tinder.com/"
DRIVER_PATH = "/Users/utkarshvarma/Dropbox/My Mac (UTKARSHs-MacBook-Pro.local)/Documents/Development/chromedriver"

driver = webdriver.Chrome(DRIVER_PATH)
driver.get(URL)

sleep(5)
login_button = driver.find_element_by_xpath(
    '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login_button.click()
sleep(5)
facebook_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]')
facebook_button.click()
sleep(5)
driver.window_handles  # Returns All the active windows connected to the browser /its called window handles
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
sleep(5)
email = driver.find_element_by_id("email")
email.send_keys(LOGIN_ID)
passowrd = driver.find_element_by_id("pass")
passowrd.send_keys(LOGIN_PASS)
passowrd.send_keys(Keys.ENTER)
driver.switch_to.window(base_window)
sleep(5)
driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()  # Allow Pop-Up
sleep(5)
driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
sleep(5)
driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()
sleep(10)
i = 0
while True:
    try:
        like = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like.click()
        if i == 0:
            sleep(4)
            driver.find_element_by_xpath('/html/body/div[2]/div/div/button[2]').click()
            sleep(4)

        sleep(2)
        i += 1
        if i == 10:
            break
    except:
        driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').send_keys(
            Keys.ESCAPE)
