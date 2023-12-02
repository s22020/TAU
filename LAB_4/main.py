from chrome_wow import ChromeWow
from firefox_wow import FirefoxWow
from chrome_tawerna import ChromeTawerna

chrome_wow = ChromeWow()
chrome_wow.run_add_product_to_cart_and_ship_test()

chrome_tawerna = ChromeTawerna()
chrome_tawerna.run_failed_login_flow()