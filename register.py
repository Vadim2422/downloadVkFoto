
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


login = "+79042193666"
password = "48VaDBr48"


def reg(driver):
    driver = driver
    driver.maximize_window()
    driver.get("https://vk.com")

    Wait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[class='VkIdForm__input']"))).send_keys(login)
    Wait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          "button[class='FlatButton FlatButton--primary FlatButton--size-l FlatButton--wide VkIdForm__button VkIdForm__signInButton']"))).click()
    Wait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']"))).send_keys(password)
    Wait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          "button[class='vkc__Button__container vkc__Button__primary vkc__Button__fluid']"))).click()

    Wait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@class = 'left_row'][1]")))
