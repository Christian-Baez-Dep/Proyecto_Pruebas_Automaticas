from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import time


class Follow_Someone():
    
    def __init__(self) -> None: 
        pass

    def Follow(driver):
        time.sleep(2)
        button_element = driver.find_element(By.XPATH, "//button[@class=' _acan _acap _acas _aj1- _ap30' and @type='button']")
        button_element.click()
        time.sleep(2)
        driver.save_screenshot('Paginas/results/test_follow.png')
