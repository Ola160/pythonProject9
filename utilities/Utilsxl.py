import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Excel file with credentials
excel_file = '/Users/olatundeolawoyin/PycharmProjects/pythonProject9/TestData/amazon-log1.xlsx'

wb = load_workbook(excel_file)
sheet = wb.active

# Read username and password from the Excel sheet
username = sheet['A1'].value
password = sheet['B1'].value

driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get('https://www.amazon.co.uk/')

    sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'nav-link-accountList')))
    sign_in_button.click()

    email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ap_email"]')))
    email_field.send_keys(username)

    continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
    continue_button.click()

    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ap_password"]')))
    password_field.send_keys(password)

    sign_in_submit = driver.find_element(By.XPATH, '//*[@id="signInSubmit"]')
    sign_in_submit.click()

    time.sleep(10)

except Exception as e:
    print("An error occurred:", e)

finally:

    driver.quit()
