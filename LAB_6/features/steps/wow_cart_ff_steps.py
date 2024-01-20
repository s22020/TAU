import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import ActionChains
from subprocess import getoutput
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then, step
import unittest

class FirefoxWow:
    def __init__(self):
        self.options = Options()
        self.options.binary_location = getoutput("find /snap/firefox -name firefox").split("\n")[-1]
        self.service = Service(executable_path = getoutput("find /snap/firefox -name geckodriver").split("\n")[-1])
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0")
        self.driver = webdriver.Firefox(service=self.service, options=self.options)
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

@given("the user is on the WoW Gear website on Firefox")
def step_given_user_on_website_on_firefox(context):
    context.ff_wow = FirefoxWow()
    context.ff_wow.logger.info("Open WoW Gear URL")
    context.ff_wow.driver.get(context.ff_wow.url)
    sleep(4)

@when("the user closes the promo popup on Firefox")
def step_when_user_closes_promo_popup_on_firefox(context):
    context.ff_wow.logger.info("Get rid of a promo popup")
    popup_close = WebDriverWait(context.ff_wow.driver,12).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".klaviyo-close-form")))
    sleep(5)
    popup_close.click()
    sleep(5)

@step("searches for a product with keyword '{keyword}' on Firefox")
def step_and_searches_for_product(context, keyword):
    context.ff_wow.logger.info("Search for a product")
    random_click = context.ff_wow.driver.find_element(By.CSS_SELECTOR, ".currency-block")
    random_click.click()
    sleep(1)
    random_click.click()
    sleep(1)
    q = context.ff_wow.driver.find_elements(By.NAME, 'q')[1]
    sleep(2)
    q.click()
    sleep(1)
    q.click()
    sleep(2)
    q.send_keys(keyword)
    sleep(1)
    context.ff_wow.driver.find_elements(By.CSS_SELECTOR, "button[type='submit']")[1].submit()
    sleep(5)

@then("the search is successful on Firefox")
def step_then_search_successful_on_firefox(context):
    context.ff_wow.logger.info("Check if search was successfull")
    search_successfull = context.ff_wow.driver.find_element(By.CSS_SELECTOR, ".search-page>.container>.page-header>h1>span:nth-child(3)").text
    tc = unittest.TestCase()
    tc.assertEqual("REVEALED THE FOLLOWING:", search_successfull)

@when("the user clicks on the first returned product on Firefox")
def step_when_user_clicks_first_product_on_firefox(context):
    context.ff_wow.logger.info("Click on first returned product")
    context.ff_wow.driver.find_element(By.CSS_SELECTOR, ".product-collection>div>div:nth-child(1)").click()

@step("adds the product to the cart on Firefox")
def step_and_adds_product_to_cart_on_firefox(context):
    context.ff_wow.logger.info("Add product to cart")
    context.ff_wow.driver.find_element(By.CSS_SELECTOR, "#product-add-to-cart").click()
    sleep(2)

@step("proceeds to checkout on Firefox")
def step_and_proceeds_to_checkout_on_firefox(context):
    context.ff_wow.logger.info("Checkout")
    context.ff_wow.driver.find_element(By.CSS_SELECTOR, ".btn-checkout").click()
    sleep(2)

@step("adds shipping details on Firefox")
def step_and_adds_shipping_details_on_firefox(context):
    context.ff_wow.logger.info("Add shipping details")
    context.ff_wow.driver.find_element(By.CSS_SELECTOR, "#checkout_email").send_keys("john.doe@example.com")
    sleep(1)
    context.ff_wow.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_first_name").send_keys("John")
    sleep(1)
    context.ff_wow.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_last_name").send_keys("Doe")
    sleep(1)
    context.ff_wow.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_address1").send_keys("Targ Drzewny")
    sleep(2)
    context.ff_wow.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_address2").send_keys("9/11")
    sleep(2)
    context.ff_wow.driver.find_elements(By.CSS_SELECTOR, ".ui-button-text")[0].click()
    context.ff_wow.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_city").send_keys("Gdansk")
    sleep(1)
    context.ff_wow.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_zip").send_keys("80-001")
    sleep(1)
    context.ff_wow.driver.find_element(By.CSS_SELECTOR, "#checkout_shipping_address_phone").send_keys("+48606606606")
    sleep(1)
    context.ff_wow.driver.find_element(By.CSS_SELECTOR, "#continue_button").submit()
    sleep(2)

@step("continues to payment on Firefox")
def step_and_continues_to_payment_on_firefox(context):
    context.ff_wow.logger.info("Continue to payment")
    context.ff_wow.driver.find_element(By.CSS_SELECTOR, "#continue_button").submit()
    sleep(2)
    
@then("the checkout is completed successfully on Firefox")
def step_then_checkout_completed_on_firefox(context):
    context.ff_wow.logger.info("Continue to payment")
    context.ff_wow.driver.find_element(By.CSS_SELECTOR, "#continue_button").submit()
    sleep(2)

    context.ff_wow.driver.quit()
