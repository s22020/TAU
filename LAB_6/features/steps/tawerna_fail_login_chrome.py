import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from behave import given, when, then

class ChromeTawerna:
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

@given("the user opens Tawerna RPG forum URL")
def step_given_user_opens_tawerna_url(context):
    context.chrome_tawerna = ChromeTawerna()
    context.chrome_tawerna.logger.info("Open Tawerna RPG forum URL")
    context.chrome_tawerna.driver.get(context.chrome_tawerna.url)
    sleep(4)

@when("the user clicks on the login button")
def step_when_user_clicks_login_button(context):
    context.chrome_tawerna.logger.info("Click login")
    context.chrome_tawerna.driver.find_element(By.CSS_SELECTOR, '.header-login>form>h5>a').click()
    sleep(2)

@when("types fake login and password")
def step_when_user_types_fake_credentials(context):
    context.chrome_tawerna.logger.info("Type fake login and password")
    context.chrome_tawerna.driver.find_element(By.CSS_SELECTOR, "#login .panel2 .inner .content .fields1>dl>dd>input[name='username']").send_keys("test-user")
    sleep(1)
    context.chrome_tawerna.driver.find_element(By.CSS_SELECTOR, "#login .panel2 .inner .content .fields1>dl>dd>input[name='password']").send_keys("test-password")
    sleep(2)
    context.chrome_tawerna.driver.find_element(By.CSS_SELECTOR, ".responsive-dd-button").click()
    sleep(5)

@then("the user sees an error message about incorrect credentials")
def step_then_user_sees_error_message(context):
    context.chrome_tawerna.logger.info("Verify error message")
    error = context.chrome_tawerna.driver.find_element(By.CSS_SELECTOR, ".error").text.split(" ")[1]
    tc = unittest.TestCase()
    tc.assertEqual("nieprawidłową", error)
    