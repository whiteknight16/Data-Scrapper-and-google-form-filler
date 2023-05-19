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
driver=webdriver.Chrome(executable_path=chrom_driver_path)
for i in range(len(address_list)):
    address=" ".join(address_list[i].getText())
    price=" ".join(price_list[i].getText().strip("₹"))
    driver.get(FORM_LINK)
    time.sleep(3)
    add=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]')
    add.send_keys(address)
    pr=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]')
    pr.send_keys(pr)
