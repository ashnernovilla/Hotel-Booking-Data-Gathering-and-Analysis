# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 19:57:38 2025

@author: ASHNER_NOVILLA
"""

import pandas as pd
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.by import By

from datetime import datetime, timedelta

import requests

import time

import sqlite3

date_now = input("Enter the Date Starting today with a format YYYY-mm-dd: ")
date_tomm = input("Enter the Date of Checkout with a format YYYY-mm-dd:: ")


input_city = input("Please put a City for the following Manila or Davao: ")

if input_city == "Manila":
    website_link = f'''https://www.booking.com/searchresults.en-gb.html?ss=Manila%2C+Philippines&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaLQBiAEBmAEJuAEXyAEM2AEB6AEBiAIBqAIDuAKw5NbBBsACAdICJGM3NjRiZjZhLTUzMzctNDQzMi04Mzc4LTg5ZDhiMDM5NGU0ZdgCBeACAQ&sid=fad79109b6f71fe7ae5a418841073733&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=-2437894&dest_type=city&checkin={date_now}&checkout={date_tomm}&group_adults=2&no_rooms=1&group_children=0 '''

elif input_city == "Davao":
    website_link = f'''https://www.booking.com/searchresults.en-gb.html?ss=Davao%2C+Philippines&ssne=Cebu+City&ssne_untouched=Cebu+City&label=gen173nr-1BCAEoggI46AdIM1gEaLQBiAEBmAEJuAEXyAEM2AEB6AEBiAIBqAIDuAKw5NbBBsACAdICJGM3NjRiZjZhLTUzMzctNDQzMi04Mzc4LTg5ZDhiMDM5NGU0ZdgCBeACAQ&sid=5a84d1c2c6305df0f9403eb57c64af7d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=5630&dest_type=region&ac_position=1&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=23275556e35c0634&ac_meta=GhAyMzI3NTU1NmUzNWMwNjM0IAEoATICZW46BERhdmFAAEoAUAA%3D&checkin={date_now}&checkout={date_tomm}&group_adults=2&no_rooms=1&group_children=0'''


r = requests.get(website_link)

if r.status_code == 200:
    print('Pass')
    
else:
    print("Fail")
    raise ExceptionType("Error Message")


driver = webdriver.Chrome()
driver.get(website_link)


time.sleep(5)

# locate_div = driver.find_elements(By.CLASS_NAME, "aa97d6032f")
locate_div = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card-container"]')

name_list = []
prices_list = []
dist_list = []
rating_list = []

for locate_place in locate_div:
    try:
        name = locate_place.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').text
        prices = locate_place.find_element(By.CSS_SELECTOR, "span[data-testid='price-and-discounted-price']").text
        dist = locate_place.find_element(By.CSS_SELECTOR, "span[data-testid='distance']").text
        rating = locate_place.find_element(By.CSS_SELECTOR, 'div[aria-hidden="true"].f63b14ab7a.dff2e52086').text

        name_list.append(name)
        prices_list.append(prices)
        dist_list.append(dist)
        rating_list.append(rating)        
    except:
        pass

driver.close()

df = pd.DataFrame(name_list, columns=['Hotel_Names'])
df['Prices'] = prices_list
df['Distances'] = dist_list
df['Rating'] = rating_list

## Dump the data to a sqlite database

conn = sqlite3.connect("hotels.db")

df.to_sql("hotel_data", conn, if_exists="replace", index=False)



## Verification that the date is actually placed in the database

# read_df = pd.read_sql("SELECT * FROM hotel_data", conn)
# print(read_df)



