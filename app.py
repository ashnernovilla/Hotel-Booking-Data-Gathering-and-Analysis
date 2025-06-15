# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 00:03:50 2025

@author: ASHNER_NOVILLA
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import numpy as np
import sqlite3

driver = webdriver.Chrome() ## Here we are going to run the slenium using google chrome search engine


## This variables are place holders
laptop_name = []
laptop_rating = []
laptop_processor = []
laptop_memory = []
laptop_os = []
laptop_storage = []
laptop_display = []
laptop_inlcusion = []
laptop_price = []
laptop_specs = []

## This is the website were we want to extract information
for page_num in range(1,3):
    page_url =f'https://www.flipkart.com/search?q=gaming+laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=gaming+laptop%7CLaptops&requestId=c1e0a154-c5dd-467f-989c-8f7b11ea8a2d&as-searchtext=gaming+&sort=price_desc&page={page_num}'
    driver.get(page_url)

    try:
        w = WebDriverWait(driver, 10)
        w.until(EC.presence_of_element_located((By.CLASS_NAME,"CGtC98")))
    except:
        driver.quit()

    laptops = driver.find_elements(By.CLASS_NAME, "CGtC98")
    for laptop in laptops:
        try:
            name = laptop.find_element(By.CLASS_NAME, "KzDlHZ").text
            rating = laptop.find_element(By.CLASS_NAME, "XQDdHH").text
            price = laptop.find_element(By.CLASS_NAME, "cN1yYO").text

        ## Splitting the lines for the price. Take the discounted price only.
            lines_price = price.splitlines()
            array_line_price = []
            for line_price in lines_price:
             array_line_price.append(lines_price[0])

            specs = laptop.find_element(By.CLASS_NAME, "G4BRas").text

        ## Splitting the lines for the specis. Divide it on OS, Storage, Memory, Display, Processor
            lines = specs.splitlines()
            array_line = []
            for line in lines:
                array_line.append(line)
            if len(array_line) == 6:

                laptop_name.append(name) ## The name of the laptop
                laptop_price.append(array_line_price[0]) ## The price of the laptop after splitting the lines
                laptop_rating.append(rating)

            ## Append per specs
                laptop_processor.append(array_line[0])
                laptop_memory.append(array_line[1])
                laptop_os.append(array_line[2])
                laptop_storage.append(array_line[3])
                laptop_display.append(array_line[4])
                laptop_inlcusion.append(array_line[5])

        except:
            pass
    sleep(5)


driver.quit()

# Creating DataFrame
data = {'Name': laptop_name,'Price': laptop_price,'Rating':laptop_rating,'Processor':laptop_processor,'RAM':laptop_memory,'Operating System':laptop_os,'Storage':laptop_storage,'Display':laptop_display,'Inclusion':laptop_inlcusion}
df = pd.DataFrame(data)
df.head()
df.info()


## Dump the data to a sqlite database

conn = sqlite3.connect("laptop.db")

df.to_sql("tbl_laptop_prices", conn, if_exists="replace", index=False)


