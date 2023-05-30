from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

USER_NAME = "YOUR EMAIL OR YOUR USER NAME"
PASSWORD = "YOUR INSTA PASSWORD"





path = "/Users/utkuozer/chromedriver"

optns = webdriver.ChromeOptions()
optns.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=optns,service=Service(executable_path=path,log_path="NUL"))

driver.get("https://www.instagram.com/")

#lang_sel = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
#lang_sel.click()
#print(lang_sel.text)

#lang_sel = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
#lang_sel.click()
#print(lang_sel.text)

time.sleep(1)

user_name_enter = driver.find_element(By. XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
user_name_enter.send_keys(USER_NAME)


password_enter = driver.find_element(By. XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
password_enter.send_keys(PASSWORD)

time.sleep(1)

login_button = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
login_button.click()

# normally commented line below worked for notifications but there is no need now.

# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'))
#     )
# element.click() 

#reason why its no working is basically xpath and elemnts are not quite good for the website.

#both works fine i commented second one.

#sometimes it takes really long time to do be carefull!

time.sleep(4)
driver.find_element(By.CSS_SELECTOR,'[aria-label="Search"]').click()


# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Search"]'))
#     )
# element.click()
time.sleep(1)
search = driver.find_element(By.CSS_SELECTOR,'[aria-label="Search input"]')
search.send_keys("kingjames")
time.sleep(1)
search.send_keys(Keys.ENTER)
search.send_keys(Keys.ENTER)

time.sleep(3)

followers = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
followers.click()
#so far it opens insagram account and its followers.

time.sleep(2)

#BELOW WORKED IT SCROLLS!

# pop_up = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, '._aano' ))
#     )
# print(pop_up)

# driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', pop_up)

#FIND FOLLOW BUTTONS ON THE DISPLAY AND FOLLOW PEOPLE.

follow_buttons = driver.find_elements(By.CSS_SELECTOR,'[type="button"]')
for button in follow_buttons:
    button.click()







