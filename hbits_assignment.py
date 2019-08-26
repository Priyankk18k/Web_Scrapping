# Importing the necessary files
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import requests
from PIL import Image
import io
import numpy as np
import pytesseract
import urllib.request
import cv2
from bs4 import BeautifulSoup
import pandas as pd

from selenium.webdriver.common.by import By




# Attaching the chrome Driver to open every time.
# We can also use firfox Driver here.



driver = webdriver.Chrome(executable_path=r'C:\Users\Priyank\PycharmProjects\selenium\chromedriver.exe')
driver.get("https://freesearchigrservice.maharashtra.gov.in")
assert "Online" in driver.title
# Getting the text fields which is to be filled.
datefieldname = "ddlFromYear"
districtfieldname = "ddlDistrict"
villagefieldname = "txtAreaName"
selectfieldvillage = "ddlareaname"
propertyfieldnumber = "txtAttributeValue"
# Filling the fields
date = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_name(datefieldname))
date.send_keys("2019")

district_name = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_name(districtfieldname))
district_name.send_keys("मुंबई उपनगर जिल्हा")
time.sleep(5)

village_name = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_name(villagefieldname))
village_name.send_keys("kole")
time.sleep(10)

property_number = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_name(propertyfieldnumber))
property_number.send_keys("4207")
time.sleep(10)

village = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_name(selectfieldvillage))
village.send_keys("Kolekalyan")
time.sleep(5)

property_number = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_name(propertyfieldnumber))
property_number.send_keys("4207")
time.sleep(10)

## Captcha Solution for the Automated software.
############################ FINDING CAPTCH IMAGE ##############################
# image_url = driver.find_element_by_id("imgCaptcha").get_attribute("src")
# url_response = urllib.request.urlopen(image_url)
# img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
# print("Image Array",img_array)
# cv2.imwrite("new_image.png",img_array)

###### 2nd solution to enter the Captcha letter on terminal.
# In case you are entering on website please uncomment below lines.

captcha_data = input("Please enter the Captcha here by looking into the image :-")
captcha_field = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_name("txtImg"))
captcha_field.send_keys(captcha_data)
# We can put a time.sleep(5) here to give time to enter the letter on website.
shodh_button = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_name("btnSearch"))
shodh_button.click()
time.sleep(10)

data = driver.page_source
# Using the BeautifulSoup module to get the HTML Text.
soup = BeautifulSoup(data,'lxml')
soup.prettify()

table_data = soup.find_all("table",id="RegistrationGrid")
from selenium.webdriver.common.by import By
table = driver.find_element(By.ID,"RegistrationGrid")
rows = table.find_elements(By.TAG_NAME, "tr")

datalist = []
data_list = pd.read_html(str(table_data),header=0)
dataframe = pd.DataFrame(data_list[0])
dataframe



############################################# TO get the NExt Page of the wesite and grab the tabular data from it.###################################3

# datalist = []
# for i in range(1,11):
#     new_page = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath("//*[@id='RegistrationGrid']/tbody/tr[12]/td/table/tbody/tr/td["+str(i)+"]/a"))
#     data = driver.page_source
#     soup = BeautifulSoup(data,'lxml')
#     soup.prettify()
#     table_data = soup.find_all("table",id="RegistrationGrid")
#     data_list = pd.read_html(str(table_data),header=0)
#     datalist.append(data_list)
# dataframe = pd.DataFrame(data_list[0])
    
    

 











