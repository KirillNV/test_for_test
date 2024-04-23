from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

 
link = "https://kai.ru/main"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #вынести в отедельный метод
    find_button_to_enter = browser.find_element(By.ID, "login_btn")
    find_button_to_enter.click()
    time.sleep(1)

    find_login = browser.find_element(By.ID, "_58_login")
    find_login.send_keys("NikiforovKiV")
    time.sleep(1)

    find_password = browser.find_element(By.ID, "_58_password")
    find_password.send_keys("7dep3iy3")
    time.sleep(1)

    btn_finish = browser.find_element(By.CLASS_NAME, "btn-primary")
    btn_finish.click()
    time.sleep(1)

    btn_user_name = browser.find_element(By.CLASS_NAME, "user_name")
    btn_user_name.click()

    #place_general = browser.find_element(By.CLASS_NAME, "open selected")
    #place_general.click()

    family_of_general = browser.find_element(By.CSS_SELECTOR, "level-2:nth-child(2)")
    family_of_general.click()

finally:
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
