from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass
from parser import parse_tickets
from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
import os
import sys

login_URL = "https://nederland.eforcesoftware.net/eFORCECommand/Account/Login.aspx?redirect=/eforcecommand/"

parse_tickets()

username = input("EForce user email: ")
password = getpass("Password: ")
driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get(login_URL)
print("URL title: " + driver.title)

#find our elements
username_box = driver.find_element(By.ID, "txtUsername")
password_box = driver.find_element(By.ID, "txtPassword")
login_button = driver.find_element(By.XPATH, '//*[@id="MainContent_btnLogin"]')
#send keys to the input boxes

username_box.send_keys(username)
password_box.send_keys(password)
#click the submit button
login_button.click()

#driver.quit()