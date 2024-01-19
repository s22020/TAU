import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from behave import given, when, then, step

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

@given("the user is on the WoW Gear website")
def step_given_user_on_website(context):
    context.chrome_wow = ChromeWow()
    context.chrome_wow.logger.info("Open WoW Gear URL")
    context.chrome_wow.driver.get(context.chrome_wow.url)
    sleep(4)

@when("the user searches for a product with keyword '{keyword}'")
def step_when_user_searches_for_product(context, keyword):
    context.chrome_wow.logger.info("Search for a product")
    context.chrome_wow.driver.find_element(By.NAME, 'q').send_keys(keyword)
    context.chrome_wow.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").submit()

@then("the search is successful")
def step_then_search_successful(context):
    context.chrome_wow.logger.info("Check if search was successful")
    search_successfull = context.chrome_wow.driver.find_element(By.CSS_SELECTOR, ".search-page>.container>.page-header>h1>span:nth-child(3)").text
    tc = unittest.TestCase()
    tc.assertEqual("REVEALED THE FOLLOWING:", search_successfull)


@when("the user clicks on the first returned product")
def step_when_user_clicks_first_product(context):
    context.chrome_wow.logger.info("Click on first returned product")
    context.chrome_wow.driver.find_element(By.CSS_SELECTOR, ".product-collection>div>div:nth-child(1)").click()
    sleep(2)

@step("adds the product to the cart")
def step_and_adds_product_to_cart(context):
    context.chrome_wow.logger.info("Add product to cart")
    context.chrome_wow.driver.find_element(By.CSS_SELECTOR, "#product-add-to-cart").click()
    sleep(2)

@step("closes the promo popup")
def step_and_closes_promo_popup(context):
    context.chrome_wow.logger.info("Get rid of a promo popup")
    popup_close = WebDriverWait(context.chrome_wow.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".klaviyo-close-form")))
    popup_close.click()
    sleep(2)

@step("proceeds to checkout")
def step_and_proceeds_to_checkout(context):
    context.chrome_wow.logger.info("Checkout")
    context.chrome_wow.driver.find_element(By.CSS_SELECTOR, ".btn-checkout").click()
    sleep(2)

@step("adds shipping details")
def step_and_adds_shipping_details(context):
    context.chrome_wow.logger.info("Add shipping details")
    context.chrome_wow.driver.find_element(By.CSS_SELECTOR, "#checkout_email").send_keys("john.doe@example.com")
    sleep(1)
    context.chrome_wow.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_first_name").send_keys("John")
    sleep(1)
    context.chrome_wow.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_last_name").send_keys("Doe")
    sleep(1)
    context.chrome_wow.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_address1").send_keys("Targ Drzewny")
    sleep(2)
    context.chrome_wow.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_address2").send_keys("9/11")
    sleep(2)
    context.chrome_wow.driver.find_elements(By.CSS_SELECTOR, ".ui-button-text")[0].click()
    context.chrome_wow.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_city").send_keys("Gdansk")
    sleep(1)
    context.chrome_wow.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_zip").send_keys("80-001")
    sleep(1)
    context.chrome_wow.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_phone").send_keys("+48606606606")
    sleep(1)
    context.chrome_wow.driver.find_element(By.CSS_SELECTOR, "#continue_button").submit()
    sleep(2)

@step("continues to payment")
def step_and_continues_to_payment(context):
    context.chrome_wow.logger.info("Continue to payment")
    context.chrome_wow.driver.find_element(By.CSS_SELECTOR, "#continue_button").submit()
    sleep(2)
    
@then("the checkout is completed successfully")
def step_then_checkout_completed(context):
    context.chrome_wow.logger.info("Continue to payment")
    context.chrome_wow.driver.find_element(By.CSS_SELECTOR, "#continue_button").submit()
    sleep(2)

    context.chrome_wow.driver.quit()
