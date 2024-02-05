# Importing the libraries
import os
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
cService = webdriver.ChromeService(executable_path='E:\SeleniumDrivers\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service = cService)

# wait time
driver.implicitly_wait(30)

# Opening the website
driver.get("https://auth.accasoftware.com/auth/realms/ACCA/protocol/openid-connect/auth?client_id=usbim-platform&redirect_uri=https%3A%2F%2Fcloud.usbim.com%2Fhome%2Fworkspaces%3Fworkspace_id%3D688815%26folder_id%3D4901695%23state%3D4db6f0cc-c3bc-461b-98f1-194830378968%26session_state%3Db4fd3f55-d958-48ea-b040-5a966a0a4a13%26code%3D2f899857-540f-40fe-9c75-04e7875dc905.b4fd3f55-d958-48ea-b040-5a966a0a4a13.73a6bf4c-671a-44d2-a78b-9b1bd57ab33f&state=2050bf51-472b-45f6-8edc-e1b08002a5cd&response_mode=fragment&response_type=code&scope=openid&nonce=7249e5f0-317a-4339-9d45-cf6f85041392&ui_locales=en")
driver.maximize_window()

# logging in
username = driver.find_element("id", "username")
password = driver.find_element("id", "password")
username.send_keys("hessamghadiri@gmail.com")
password.send_keys('james15HARDEN')
login = driver.find_element(By.ID, "kc-login")
login.click()

main_window_handle = driver.current_window_handle

# Opening the file
Open = driver.find_element(By.XPATH, '//button[@class="mat-mdc-tooltip-trigger btn-open-file mdc-icon-button mat-mdc-icon-button mat-unthemed mat-mdc-button-base ng-star-inserted"]')
Open.click()

time.sleep(2) # Wait for 2 seconds for the pop-up to open
popup_window_handle = None
while not popup_window_handle:
   for handle in driver.window_handles:
       if handle != main_window_handle:
           popup_window_handle = handle
           break
driver.switch_to.window(popup_window_handle)
time.sleep(25)

def screen_shot(dr):
    screenshot = dr.find_element(By.ID, "bni_key_Screenshot:0")
    screenshot.click()
    time.sleep(2)
    sc = dr.find_elements(By.XPATH,'//button[@class="MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButtonBase-root  css-14wq495"]')[0]
    sc.click()
    time.sleep(2)
    Cancel = dr.find_elements(By.XPATH,'//button[@class="MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButtonBase-root  css-14wq495"]')[1]
    Cancel.click()

def rotation(dr,angle):
    Rotate_model = dr.find_element(By.ID, "bni_key_transformDialog:0")
    Rotate_model.click()
    Z_Rotate = dr.find_element(By.ID, "2")
    Z_Rotate.clear()
    Z_Rotate.send_keys(angle)
    time.sleep(1)
    OK = dr.find_element(By.XPATH,'//button[@class="MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButtonBase-root  css-14wq495"]')
    OK.click()

def R_and_SC(dr,angle):
    rotation(dr,angle)
    time.sleep(1)
    screen_shot(dr)
    time.sleep(1)

R_and_SC(driver,30)
R_and_SC(driver,60)
R_and_SC(driver,90)
R_and_SC(driver,120)

