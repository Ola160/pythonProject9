import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage

# Define the base URL and other constants
baseURL = "https://www.amazon.co.uk/"
username = "olawohoney@yahoo.com"
password = "Aramide247!"


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()

@pytest.mark.usefixtures("setup")
class TestAmazon:
    def setUp(self):
        self.driver = setup
        self.lp = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()


    def test_AmazonhomePage(self):
        self.driver.get(baseURL)
        self.lp = LoginPage(self.driver)
        act_title = self.driver.title
        assert "Amazon" in act_title

    def test_amazon_login(self):
        self.driver.get(baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(username)
        time.sleep(3)
        self.lp.clickContinue()
        self.lp.setPassword(password)
        self.lp.clickLogin()
        act_title = self.driver.title
        assert "Dashboard" in act_title

    def test_search_item(self):
        self.driver.get(baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.searchItem()
        search_element = self.driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
        time.sleep(5)
        search_element.send_keys("headphones")

    def test_add_to_cart(self):
        self.driver.get("https://www.amazon.co.uk/s?k=headphones&crid=BR218O369WW9&sprefix=%2Caps%2C244&ref=nb_sb_ss_recent_1_0_recent")
        self.lp.add_to_cart()
        self.add_to_cart = self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]')
        time.sleep(3)
        self.driver = setup
        self.lp = LoginPage(self.driver)


