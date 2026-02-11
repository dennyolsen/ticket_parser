# Usage: python driver.py [directory to be scanned]

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from getpass import getpass
from selenium.webdriver.common.keys import Keys
from parser import parse_tickets
import sys
import settings

args = sys.argv
tickets_dir = args[1]

#login_URL = "https://nederland.eforcesoftware.net/eFORCECommand/Account/Login.aspx?redirect=/eforcecommand/"
visual = True
#firefox_binary = r'C:\Program Files\WindowsApps\Mozilla.Firefox_147.0.3.0_x64__n80bbvh6b1yt2\VFS\ProgramFiles\Firefox Package Root\firefox.exe'
tickets_data = parse_tickets()

print(tickets_data)

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

#Enter RMS
rms_button = driver.find_element(By.ID, "RMS_LaunchAppButton") 
rms_button.click()
driver.switch_to.new_window('tab')
driver.get("https://nederland.eforcesoftware.net/RMS/RMS/Entry/citations/citationsBegin.aspx")

#Start eCitation Entry
dropdown_button = driver.find_element(By.ID, "select2-chosen-7") 
dropdown_button.click()
dropdown_input = driver.find_element(By.ID, "s2id_autogen7_search")
dropdown_input.send_keys("BCSO ECITATION")
dropdown_input.send_keys(Keys.ENTER)
citation_number_input = driver.find_element(By.ID, "ctl00_contentBody_txtCitationNumber")
citation_number_input.send_keys("TEST128")
driver.implicitly_wait(5)
submit_button = driver.find_element(By.ID, "ctl00_contentBody_btnManualCitation") 
submit_button.click()
driver.implicitly_wait(5)
create_button = driver.find_element(By.ID, "ctl00_contentBody_ctl01") 
create_button.click()
# no = ctl00_contentBody_ctl02
# yes = ctl00_contentBody_ctl01

#Citation Info
date_cited = driver.find_element(By.ID, "dtCited_startDate")
date_cited.click()
date_cited.clear()
driver.implicitly_wait(5)
date_cited.send_keys("12/20/2025")
date_cited.send_keys(Keys.ENTER)
MVstop = driver.find_element(By.ID, "rblTypes_2")
#driver.execute_script("arguments[0].scrollIntoView(true);", MVstop)
#MVstop.click()
#driver.implicitly_wait(5)
CDL = driver.find_element(By.ID, "select2-chosen-6")
driver.execute_script("arguments[0].scrollIntoView(true);", CDL)
driver.implicitly_wait(5)
CDL.click()
CDL.send_keys("NO ")
CDL.send_keys(Keys.ENTER)
traffic_vio = driver.find_element(By.ID, "ctl00_ctl00_contentBody_body_rptCustomFields_ctl14_chk")
traffic_vio.click()
save_btn = driver.find_element(By.ID, "btnSave")
save_btn.click()

#Charges
charges = driver.find_element(By.ID, "s2id_search")
charges.click()
charges.clear()
driver.implicitly_wait(5)
charges.send_keys("1101")
driver.implicitly_wait(5)
charges.send_keys(Keys.ENTER)
add_charge_btn = driver.find_element(By.ID, "ctl00_ctl00_contentBody_body_btnAddArrestCode")
add_charge_btn.click()
save_charge_btn = driver.find_element(By.ID, "ctl00_ctl00_contentBody_body_btnSave")
save_charge_btn.click()

#Involved
last_name = driver.find_element(By.ID, "txtDnaLast") 
charges.click()
charges.clear()
driver.implicitly_wait(5)
charges.send_keys("lastName")
first_name = driver.find_element(By.ID, "txtDnaFirst") 
first_name.click()
first_name.clear()
driver.implicitly_wait(5)
first_name.send_keys("firstName")
dob = driver.find_element(By.ID, "dtDOB_startDate") 
dob.click()
dob.clear()
driver.implicitly_wait(5)
dob.send_keys("01/01/2021")












if visual:
    input("Press Enter to continue...")

if visual == False:
    driver.quit()