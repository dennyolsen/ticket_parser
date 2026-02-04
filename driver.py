from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from getpass import getpass
from selenium.webdriver.common.keys import Keys
#from parser import parse_tickets

login_URL = "https://nederland.eforcesoftware.net/eFORCECommand/Account/Login.aspx?redirect=/eforcecommand/"
visual = True
firefox_binary = r'C:\Program Files\WindowsApps\Mozilla.Firefox_147.0.2.0_x64__n80bbvh6b1yt2\VFS\ProgramFiles\Firefox Package Root\firefox.exe'

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

rms_button = driver.find_element(By.ID, "RMS_LaunchAppButton") 
rms_button.click()
driver.switch_to.new_window('tab')
driver.get("https://nederland.eforcesoftware.net/RMS/RMS/Entry/citations/citationsBegin.aspx")

dropdown_button = driver.find_element(By.ID, "select2-chosen-7") 
dropdown_button.click()
dropdown_input = driver.find_element(By.ID, "s2id_autogen7_search")
dropdown_input.send_keys("BCSO ECITATION")
dropdown_input.send_keys(Keys.ENTER)
citation_number_input = driver.find_element(By.ID, "ctl00_contentBody_txtCitationNumber")
citation_number_input.send_keys("C00010037E")
citation_number_input.send_keys(Keys.ENTER)


if visual:
    input("Press Enter to continue...")

if visual == False:
    driver.quit()