# the code is hosted on github.com/engineervinay if you wanted to make development in code visit profile and fork the code
# if you have any query related to this code you can contact me on github @engineervinay & @theuitown

# importing keys from selenium to enter the comments
import random
#
# import wb as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# time library for sleepcommand
from time import sleep

# library to provide random integer values between range
from random import randint

from selenium import webdriver

from sys import platform

# window to accept inputs username, password, and hashtags
user = input("Enter username: ")
passw = input("Enter password: ")
hash = input("enter hashtags seperated by , : ")

# Change this to your own chromedriver path!
if platform=='linux' or platform=='linux2':
    binary = FirefoxBinary('/usr/lib/firefox/firefox')
    webdriver = webdriver.Firefox(firefox_binary=binary)
elif platform=='darwin':
    binary = FirefoxBinary('path/to/installed firefox binary')
    webdriver = webdriver.Firefox(firefox_binary=binary)
elif platform=='win32':
    chromedriver_path = '/home/iamharsh/Downloads/chromedriver'
    webdriver = webdriver.Chrome(executable_path=chromedriver_path)

sleep(2)
# opening instagram login page
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

sleep(3)

username = webdriver.find_element_by_name('username')  # finding username inputbox

username.send_keys(user)  # pasaing username

password = webdriver.find_element_by_name('password')
password.send_keys(passw)

# finfing ligin button
button_login = webdriver.find_element_by_css_selector(
    '#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child() > button')
# clicking on button
button_login.click()

sleep(3)

# clicking on not now button which occurs when we logged in
notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click()

hashtag_list1 = hash.split(",")
for hashtag in hashtag_list1:

    sleep(5)
    webdriver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')

    sleep(5)

    first_thumbnail = webdriver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
    first_thumbnail.click()

    sleep(randint(1, 2))

    for x in range(1, 200):

        # username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text
        # if username not in prev_user_list:
        # If we already follow, do not unfollow

        # if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':

        # webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()

        # new_followed.append(username)

        # followed += 1

        # Liking the picture
        sleep(randint(3, 7))
        # finding the like button using xpath
        button_like = webdriver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')

        button_like.click()  # cliking on founded like button to like photo

        comm_prob = randint(1, 4)
        stMsgs = ["That brow game, though.", 'Stunning', 'Nice!', 'Awesome Pic:) ']
        stMsgs2=['Dammmmmmmnnnn.', 'Amazing !', 'Impressive picture', 'Adorable picture.']
        stMsgs3=['It looks lovely', 'Looks great', 'This picture is lit!!', 'This picture made my day.']
        stMsgs4=['\U0001F525'+'\U0001F525'+'\U0001F525', 'All I have to say is '+'\U0001F525', 'One word: stunning.', 'Can I have this picture framed?']
        print(random.choice(stMsgs))
        # to enable commenting box
        webdriver.find_element_by_xpath(
            '/html/body/div[]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click()
        # clicking on comment box
        comment_box = webdriver.find_element_by_xpath(
            '/html/body/div[]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
        sleep(randint(3, 7))
        # code to post random comments
        if comm_prob == 1:
            # this statement will send the comment to the comment box
            comment_box.send_keys(random.choice(stMsgs))
            sleep(5)

        elif comm_prob == 2:

            comment_box.send_keys(random.choice(stMsgs2))

            sleep(5)

        elif comm_prob == 3:

            comment_box.send_keys(random.choice(stMsgs3))

            sleep(5)

        elif comm_prob == 4:

            comment_box.send_keys(random.choice(stMsgs4))

            sleep(5)

        sleep(randint(4, 6))
        comment_box.send_keys(Keys.ENTER)  # Enter to post comment
        sleep(randint(22, 28))

        webdriver.find_element_by_link_text('Next').click()  # clicking on next for next photo
        sleep(randint(25, 29))

# Developed by vinay patil & few modifications by HARSH VARDHAN GOSWAMI
