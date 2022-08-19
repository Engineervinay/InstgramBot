# the code is hosted on github.com/engineervinay if you wanted to make development in code visit profile and fork the code
# if you have any query related to this code you can contact me on github @engineervinay

import random
import time
from time import sleep
from random import randint
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def next_image():
    try:
        wait_xpath('//div/div/div/div/div[1]/div/div/div[2]/button')
        driver.find_element(By.XPATH, '//div/div/div/div/div[1]/div/div/div[2]/button').click()
    except:
        wait_xpath('//div/div/div/div/div[1]/div/div/div[1]/button')
        driver.find_element(By.XPATH, '//div/div/div/div/div[1]/div/div/div[1]/button').click()
    sleep(3)


def wait_xpath(xpath, sec: int = 20):
    WebDriverWait(driver, sec).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )


def wait_CSS(selector, sec: int = 20):
    WebDriverWait(driver, sec).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )


def wait_NAME(name, sec: int = 20):
    WebDriverWait(driver, sec).until(
        EC.presence_of_element_located((By.NAME, name))
    )

# window to accept inputs username, password, and hashtags
# user = input("enter username:")
# passwrd = input("enter password:")
# hashtags = input("enter hashtags seperated by , :")


user = 'h_shadowpro'
passwrd = 'Osama123'
hashtags = 'python'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
action = webdriver.ActionChains(driver)

sleep(2)
# opening instagram login page.
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

wait_NAME('username')
username = driver.find_element(By.NAME, 'username')  # finding username inputbox
username.send_keys(user)  # passing username.

wait_NAME('password')
password = driver.find_element(By.NAME, 'password')
password.send_keys(passwrd)
# finding login button

wait_CSS('#loginForm > div > div:nth-child(3) > button')
button_login = driver.find_element(By.CSS_SELECTOR,
                                   '#loginForm > div > div:nth-child(3) > button')
button_login.click()

try:
    wait_xpath('//*[@id="slfErrorAlert"]', 3)
    driver.find_element(By.XPATH, '//*[@id="slfErrorAlert"]')
    print("Too many login Trials, exit")
    quit()
except:
    pass

#  check if we are logged in

wait_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]')

# clicking on not now button which occurs when we logged in # Not Always
try:
    notnow = driver.find_element(By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
    notnow.click()
except:
    pass

hashtag_list = hashtags.strip().split(",")  # remove any spaces with strip()
for hashtag in hashtag_list:

    driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')

    for i in range(4):  # sometimes the page doesn't load currently, so we refresh it
        try:
            wait_xpath('//article/div[1]/div/div/div[1]/div[1]')
        except:
            driver.refresh()
            if i == 3:
                exit()

    first_thumbnail = driver.find_element(By.XPATH,
                                          '//article/div[1]/div/div/div[1]/div[1]')
    first_thumbnail.click()
    sleep(randint(1, 2))

    for x in range(1, 100):

        # Liking the picture
        sleep(3)
        # finding the like button using xpath

        try:  # if the photo is already liked => skip
            wait_xpath('//article/div/div[2]/div/div/div[2]/section[1]/span[1]/button/div[2]/span', 5)
            button_like = driver.find_element(By.XPATH,
                                              '//article/div/div[2]/div/div/div[2]/section[1]/span[1]/button/div[2]/span')
            button_like.click()  # cliking on founded like button to like photo
        except:
            next_image()
            continue

        comm_prob = randint(1, 2)
        # to enable commenting box
        driver.find_element(By.XPATH, '//article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea').click()
        # clicking on comment box
        comment_box = driver.find_element(By.XPATH,
                                          '//article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
        sleep(1)
        # code to post random comments
        list_of_comments = ['So cool! :)', 'Mind Blowing!!', 'Nice work :)', 'Really cool!']

        comment = random.choice(list_of_comments)
        comment_box.send_keys(comment)
        sleep(randint(1, 3))
        comment_box.send_keys(Keys.ENTER)  # Enter to post comment
        sleep(3)
        next_image()

# Developed by vinay patil
