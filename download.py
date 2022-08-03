import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from register import reg

URL = 'https://vk.com/chereshnevavictoria'
path = "/home/vadim/foto3"


def get_link(driver_chrome):
    return Wait(driver_chrome, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='pv_photo'] img"))).get_attribute("src")


def save(url, path):
    img = requests.get(url)
    img_file = open(path, 'wb')
    img_file.write(img.content)
    img_file.close()


def next_foto(driver_chrome):
    Wait(driver_chrome, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='pv_photo'] img"))).click()


driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()
reg(driver)
window = f'window.open("{URL}")'
driver.execute_script(window)
driver.close()
driver.switch_to.window(driver.window_handles[0])

Wait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, "//a[@class = 'page_square_photo crisp_image '][1]"))).click()

first_link = get_link(driver)
i = 1
while True:
    save(get_link(driver), path + f"/img{i}")
    i = i + 1
    next_foto(driver)
    if get_link(driver) == first_link:
        break
driver.quit()
