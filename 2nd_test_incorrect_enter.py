from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://kai.ru/main"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_button_to_enter = browser.find_element(By.ID, "login_btn")
    find_button_to_enter.click()
    time.sleep(1)

    find_login = browser.find_element(By.ID, "_58_login")
    find_login.send_keys("InCorrect")
    time.sleep(1)

    find_password = browser.find_element(By.ID, "_58_password")
    find_password.send_keys("1234abcd")
    time.sleep(1)

    btn_finish = browser.find_element(By.CLASS_NAME, "btn-primary")
    btn_finish.click()
    time.sleep(3)

    try:
        browser.find_element(By.CLASS_NAME, "user_name")

    except:
        print('Ошибка при входе')

finally:
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
