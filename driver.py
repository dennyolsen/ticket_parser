from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from getpass import getpass
#from parser import parse_tickets

login_URL = "https://nederland.eforcesoftware.net/eFORCECommand/Account/Login.aspx?redirect=/eforcecommand/"
visual = True
firefox_binary = r'/usr/bin/firefox'

#parse_tickets()  commenting this out until we get it running on Windoze

username = input("EForce username: ")
password = getpass("Password: ")
options = Options()
options.binary_location = firefox_binary
if visual == False:
    options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(5)
driver.get(login_URL)

#find our elements
username_box = driver.find_element(By.ID, "txtUsername")
password_box = driver.find_element(By.ID, "txtPassword")
login_button = driver.find_element(By.XPATH, '//*[@id="MainContent_btnLogin"]')
#send keys to the input boxes

username_box.send_keys(username)
password_box.send_keys(password)
#click the submit button
login_button.click()

if visual:
    input("Press Enter to continue...")

# rms_button = driver.find_element(By.ID, "txtUsername") <===== make this work once past authentication

if visual == False:
    driver.quit()