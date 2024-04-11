from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import time


class Watch_History():
    
    def __init__(self) -> None: 
        pass

    def Watch(driver):
        button_element = driver.find_element(By.XPATH, "//div[@class='_aarf x1e56ztr x1gslohp' and @aria-disabled='true' and @role='button']")
        button_element.click()
        time.sleep(3)
        driver.save_screenshot('Paginas/results/test_history.png')
