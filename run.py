from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


from faker import Faker 

fake = Faker()
opts = Options()
opts.headless = False
opts.add_argument('log-level=3')
# email = pd.read_csv('baru.csv')   
 

opts.add_argument('--disable-blink-features=AutomationControlled')


email = "jatiellis6@an002.lordjanu.com"
password = "admin123"

def check_out():
    global browser
    global element
    print("[*] Trying to shop")
    browser.get('https://www.aliexpress.com/item/4000123733692.html?spm=a2g0o.cart.0.0.234b3c00lWc554&mp=1')
    sleep(5)
    
    element = wait(browser,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div[2]/div/div[2]/div[7]/div/div[1]/ul/li[1]/div/img")))
    element.click()

    sleep(0.5)

    element = wait(browser,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div[2]/div/div[2]/div[7]/div/div[2]/ul/li[1]/div")))
    element.click()
    
    sleep(0.3)
    print("[*] Trying to Buy Now")
    element = wait(browser,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div[2]/div/div[2]/div[11]/span[1]/button")))
    element.send_keys(Keys.ENTER)
    
    print("[*] Trying to Click Method Payment")
    element = wait(browser,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/button")))
    element.send_keys(Keys.ENTER)
    
    print("[*] Trying to Click Web Money")
    element = wait(browser,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div[3]/div")))
    element.click()

    print("[*] Trying to Click Place Order")
    element = wait(browser,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/button")))
    element.send_keys(Keys.ENTER)
    
def email1():
    global email
    global password
    global element
    global browser
    browser.save_screenshot("after.png")
    element = wait(browser,20).until(EC.presence_of_element_located((By.ID, 'identifierId')))

def entar_email():
    global email
    global password
    global element
    global browser
    try:

        email1()
    except:
        browser.refresh()
        email1()
    else:
        print("[*] Input Email")
        element.send_keys(email)
        element.send_keys(Keys.ENTER)

    try:    
        sleep(0.5)
        element = wait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")))
        print("[*] Input Password")
        element.send_keys(password)
        element.send_keys(Keys.ENTER)       
        sleep(30)
        print("[*] Go to Aliexpress")
        check_out()

    except Exception as e:
        sleep(2)
        print(e)

def open_browser():
    global browser
    browser = webdriver.Chrome(options=opts, executable_path=r"C:\Users\User\Downloads\chrome\chromedriver.exe")
    browser.get('https://login.aliexpress.com/express/buyer_login_new.htm')
   
    element = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/section/div/div[2]/a')))
    element.click() 
    browser.switch_to.window(browser.window_handles[1])
    
    print(f"[*] Login google: {email}")
    browser.save_screenshot("before.png")
    entar_email()
    
def main():
    global email
    global password
    global browser
    print("[*] Automation Checkout Aliexpress")
    print("[*] Format: email|password")
    file_list = input("[*] Input Path File (example: D:/File.txt:  ")
    myfile = open(file_list,"r")
    list_account = myfile.read()
    list_accountsplit = list_account.split()

    for i in list_accountsplit:
          
        k = i.split("|")
        email = k[0]
        password = k[1]
        open_browser()

main()
