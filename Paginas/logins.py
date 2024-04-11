from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import time


class Make_Login():
    
    def __init__(self):
      self.driver = webdriver.Chrome()
      self.driver.get("https://www.instagram.com/")

    def login_successful(self):
        correo_textField = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.NAME,'username')))
        pass_textField = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.NAME,'password')))

        pass_textField.clear()
        correo_textField.clear()

        correo_textField.send_keys('8295028892')
        pass_textField.send_keys('Ch19102004@#$$')

        self.driver.save_screenshot('Paginas/results/test_login_succes1.png')

        iniciar = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
        iniciar.click()


        while True:
            try:
                WebDriverWait(self.driver, 10).until(EC.url_to_be("https://www.instagram.com/accounts/onetap/?next=%2F"))
                home = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a")))
                home.click()
                
                WebDriverWait(self.driver, 10).until(EC.url_to_be("https://www.instagram.com/?next=%2F"))
                button = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='_a9-- _ap36 _a9_1' and @tabindex='0']")))
                button.click()
                
                time.sleep(2)

                self.driver.save_screenshot('Paginas/results/test_login_succes2.png')

                break

            except:
                print("La página no cargó en 10 segundos.")
                break
            

    def login_failure(self):
            correo_textField = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.NAME,'username')))
            pass_textField = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.NAME,'password')))

            pass_textField.clear()
            correo_textField.clear()

            correo_textField.send_keys('kasjefbhasfgawjik@gmail.com')
            pass_textField.send_keys('8098900627A*')

            self.driver.save_screenshot('Paginas/results/test_login_fail1.png')

            iniciar = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
            iniciar.click()

            time.sleep(2)
            self.driver.save_screenshot('Paginas/results/test_login_fail2.png')
