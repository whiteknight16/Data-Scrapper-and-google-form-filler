from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
FORM_LINK="https://forms.gle/SjZ9xzaeQ3W25ghD9"
MAGIC_BRICK_LINK="https://www.magicbricks.com/flats-for-rent-in-new-delhi-pppfr"
# Creaitng Soup
data=requests.get(MAGIC_BRICK_LINK).content
soup=BeautifulSoup(data,"html.parser")
#Intializing Selium
chrom_driver_path="C:/Development/chromedriver.exe"
# Looking For Data in soup
address_list=soup.find_all("h2",class_="mb-srp__card--title")
price_list=soup.find_all("div",class_="mb-srp__card__price--amount")
option=webdriver.ChromeOptions()
option.add_argument("start-maximized")
option.add_argument("disable-infobars")
option.add_argument("--disable-extensions")
driver=webdriver.Chrome(executable_path=chrom_driver_path,options=option)
for i in range(len(address_list)):
    address=" ".join(address_list[i].getText())
    price=" ".join(price_list[i].getText().strip("₹"))
    driver.get(FORM_LINK)
    time.sleep(3)
    inputs=driver.find_elements(By.CSS_SELECTOR,'.whsOnd')
    inputs[0].send_keys(address)
    inputs[1].send_keys(price)
    time.sleep(3)
    submit_button=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
    time.sleep(2)

driver.get("https://docs.google.com/spreadsheets/d/1FgeIulaxqFkEcc8knOKY_g_4ggRR5NHZ7QM1DGvGudA/edit?resourcekey#gid=1448752214")