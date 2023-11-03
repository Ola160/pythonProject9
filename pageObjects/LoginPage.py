from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
    textbox_username_xpath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/form/div/div/div/div[1]/input[1]"
    submit_xpath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/form/div/div/div/div[1]/input[1]"
    textbox_password_xpath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div/form/div/div[1]/input"
    submit_button_xpath = "/html/body/div[1]/div[1]/div[2]/div/div2]/div/div[2]/div/form/div/div[2]/span/span/input"
    search_element = '//*[@id="twotabsearchtextbox"]'
    add_to_cart = '//*[@id="add-to-cart-button"]'

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.submit_xpath).click()

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()

    def addtoCart(self):
        self.driver.find_element(By.XPATH, self.add_to_cart).click()

    def searchItem(self):
        self.driver.find_element(By.XPATH, self.search_element).send_keys()















