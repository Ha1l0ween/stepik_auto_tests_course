from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "http://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block > div.form-group.first_class > input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block > div.form-group.second_class > input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block > div.form-group.third_class > input")
    input3.send_keys("test@mail.ru")
    input4 = browser.find_element(By.CSS_SELECTOR, ".second_block > div.form-group.first_class > input")
    input4.send_keys("89999999999")
    input5 = browser.find_element(By.CSS_SELECTOR, ".second_block > div.form-group.second_class > input")
    input5.send_keys("843495, Самарская область, город Лотошино, пл. 1905 года, 05")
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

    Registration = browser.find_element(By.TAG_NAME, "h1")
    checked = Registration.text
    print(checked)
    assert checked == "Congratulations! You have successfully registered!", "Текст об успешной регистрации не соответствует требованиям"
finally:
    time.sleep(5)
    browser.quit()