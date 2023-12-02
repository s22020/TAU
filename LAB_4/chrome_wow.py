import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class ChromeWow:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://eu.gear.blizzard.com/"
        self.logger = self._set_logger()

    def _set_logger(self):
        logger = logging.getLogger('Selenium')
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger


    def run_add_product_to_cart_and_ship_test(self):
        self.logger.info("Open WoW Gear URL")
        self.driver.get(self.url)
        sleep(4)

        self.logger.info("Search for a product")
        self.driver.find_element(By.NAME, 'q').send_keys('horde beanie')
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").submit()

        self.logger.info("Check if search was successfull")
        search_successfull = self.driver.find_element(By.CSS_SELECTOR, ".search-page>.container>.page-header>h1>span:nth-child(3)").text
        tc = unittest.TestCase()
        tc.assertEqual("REVEALED THE FOLLOWING:", search_successfull)
        
        self.logger.info("Click on first returned product")
        self.driver.find_element(By.CSS_SELECTOR, ".product-collection>div>div:nth-child(1)").click()

        self.logger.info("Get rid of a promo popup")
        popup_close = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".klaviyo-close-form")))
        popup_close.click()
        sleep(2)

        self.logger.info("Add product to cart")
        self.driver.find_element(By.CSS_SELECTOR, "#product-add-to-cart").click()
        sleep(2)

        self.logger.info("Checkout")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-checkout").click()
        sleep(2)

        self.logger.info("Add shipping details")
        self.driver.find_element(By.CSS_SELECTOR, "#checkout_email").send_keys("john.doe@example.com")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_first_name").send_keys("John")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_last_name").send_keys("Doe")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_address1").send_keys("Targ Drzewny")
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_address2").send_keys("9/11")
        sleep(2)
        self.driver.find_elements(By.CSS_SELECTOR, ".ui-button-text")[0].click()
        self.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_city").send_keys("Gdansk")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_zip").send_keys("80-001")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_phone").send_keys("+48606606606")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#continue_button").submit()
        sleep(2)

        self.logger.info("Continue to payment")
        self.driver.find_element(By.CSS_SELECTOR, "#continue_button").submit()
        sleep(2)

        self.driver.quit()
