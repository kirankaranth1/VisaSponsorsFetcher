# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import unittest, time, re

def enfOfPageOrScrollOnce():
    while True:
        e = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/span")
        if(len(e)> 0):
            print("End")    
            return
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("Scrolling")


binary_argument = FirefoxBinary(r'C:\\Program Files\\Mozilla Firefox\\firefox.exe')

capabilities_argument = DesiredCapabilities().FIREFOX
driver = webdriver.Firefox(firefox_binary=binary_argument, capabilities=capabilities_argument)
driver.implicitly_wait(1)



i = 1
driver.get("https://www.kaggle.com/jobs")
time.sleep( 1 )
enfOfPageOrScrollOnce()
URLs = []

while True:
    job = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/a["+str(i)+"]")
    if(len(job)) > 0:
        URLs.append(job[0].get_attribute('href'))
    else:
        break
    i = i+ 1

print(URLs)
for url in URLs:
    driver.get(url)
    try:
        company = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[1]/div[2]/div[2]").text
        location = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[1]/div[2]/span[3]").text
        visa = "Sponsors Visas" in driver.page_source

        if(visa):
            print("Company: " + company)
            print("Location: "+ location)
            print("Offers VISA: " + str(visa)
        )
    except:
        pass


    
