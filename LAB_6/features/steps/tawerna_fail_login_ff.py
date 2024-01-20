import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from behave import given, when, then

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

@given("the user opens Tawerna RPG forum URL on Firefox")
def step_given_user_opens_tawerna_url(context):
    context.ff_tawerna = FirefoxTawerna()
    context.ff_tawerna.logger.info("Open Tawerna RPG forum URL")
    context.ff_tawerna.driver.get(context.ff_tawerna.url)
    sleep(4)

@when("the user clicks on the login button on Firefox")
def step_when_user_clicks_login_button(context):
    context.ff_tawerna.logger.info("Click login")
    context.ff_tawerna.driver.find_element(By.CSS_SELECTOR, '.header-login>form>h5>a').click()
    sleep(2)

@when("types fake login and password on Firefox")
def step_when_types_fake_login_and_password(context):
    context.ff_tawerna.logger.info("Type fake login and password")
    context.ff_tawerna.driver.find_element(By.CSS_SELECTOR, "#login .panel2 .inner .content .fields1>dl>dd>input[name='username']").send_keys("test-user")
    sleep(1)
    context.ff_tawerna.driver.find_element(By.CSS_SELECTOR, "#login .panel2 .inner .content .fields1>dl>dd>input[name='password']").send_keys("test-password")
    sleep(2)
    context.ff_tawerna.driver.find_element(By.CSS_SELECTOR, ".responsive-dd-button").click()
    sleep(5)

@then("the user sees an error message about incorrect credentials on Firefox")
def step_then_user_sees_error_message(context):
    error = context.ff_tawerna.driver.find_element(By.CSS_SELECTOR, ".error").text.split(" ")[1]
    tc = unittest.TestCase()
    tc.assertEqual("nieprawidłową", error)
        
    context.ff_tawerna.driver.quit()
