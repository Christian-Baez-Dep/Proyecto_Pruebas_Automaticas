from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import time


class Make_Search():
    
    def __init__(self) -> None: 
        pass

    def Search(driver):
        target_anchor_xpath = driver.find_element(By.XPATH, "//a[@class='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd' and @href='#' and @role='link' and @tabindex='0']")
        target_anchor_xpath.click()
        time.sleep(3)
        
        target_input_xpath = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        target_input_xpath.clear()
        target_input_xpath.send_keys('drake')
        time.sleep(3)
        driver.save_screenshot('Paginas/results/test_search1.png')

        target_anchor_xpath = driver.find_element(By.XPATH, "//a[contains(@href, 'champagnepapi/') and @role='link' and @tabindex='0']")
        target_anchor_xpath.click()
        time.sleep(3)
        
        driver.save_screenshot('Paginas/results/test_search2.png')

