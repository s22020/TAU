import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class FirefoxTawerna:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://tawerna.rpg.pl/forum/"
        self.logger = self._set_logger()

    def _set_logger(self):
        logger = logging.getLogger('Selenium')
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger


    def run_failed_login_flow(self):
        self.logger.info("Open Tawerna RPG forum URL")
        self.driver.get(self.url)
        sleep(4)

        self.logger.info("Click login")
        self.driver.find_element(By.CSS_SELECTOR, '.header-login>form>h5>a').click()
        sleep(2)

        self.logger.info("Type fake login and password")
        self.driver.find_element(By.CSS_SELECTOR, "#login .panel2 .inner .content .fields1>dl>dd>input[name='username']").send_keys("test-user")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#login .panel2 .inner .content .fields1>dl>dd>input[name='password']").send_keys("test-password")
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".responsive-dd-button").click()
        sleep(5)

        error = self.driver.find_element(By.CSS_SELECTOR, ".error").text.split(" ")[1]
        tc = unittest.TestCase()
        tc.assertEqual("nieprawidłową", error)
        
        self.driver.quit()
