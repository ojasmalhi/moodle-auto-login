from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get("https://moodle.iitd.ac.in/login/index.php")

try:
    username = input("Username: ")
    password = input("Password: ")

    # wait until elements appear and element defn
    username_box = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_box.send_keys(username)

    password_box = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_box.send_keys(password)

    text = driver.find_element_by_id("login").text
    captcha = driver.find_element_by_id("valuepkg3")
    login = driver.find_element_by_id("loginbtn")
    words = text.split()

    # captcha clear
    captcha.clear()

    # captcha solver
    if "first" in words:
        captcha.send_keys(words[10])
    elif "second" in words:
        captcha.send_keys(words[12])
    elif "add" in words:
        add = int(words[8]) + int(words[10])
        captcha.send_keys(int(add))
    elif "subtract" in words:
        diff = int(words[8]) - int(words[10])
        captcha.send_keys(int(diff))

    # login
    login.click()

except:
    driver.quit()
