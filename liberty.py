from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs
import time
from selenium.webdriver.common.by import By


# Open Chrome browser and navigate to the page
driver = webdriver.Chrome()
driver.get("https://www.libertydentalplan.com/Find-a-Dentist/Find-a-Dentist.aspx")

state=driver.find_elements(By.NAME, ('ctl00$ContentArea$ProviderSearch1$ddlState'))
print('ok')
drp=Select(state[0])
drp.select_by_visible_text("Texas")
time.sleep(4)

network=driver.find_elements(By.ID, ('ddlNetwork'))
print('ok')
drp=Select(network[0])
drp.select_by_visible_text("Memorial Hermann")
time.sleep(4)

citybutton = driver.find_elements(By.XPATH, '/html/body/form/div[3]/main/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/a[2]')
citybutton[0].click()

city = 'Houston'
tit = driver.find_elements(By.XPATH, '//*[@id="ctl00_ContentArea_ProviderSearch1_txtCity"]')
tit[0].send_keys(city)
print('ok')
time.sleep(7)

specialist =driver.find_elements(By.ID, ('ctl00_ContentArea_ProviderSearch1_ddlSpecialists'))
print('ok')
drp=Select(specialist[0])
drp.select_by_visible_text("General Dentist")
time.sleep(10)

search = driver.find_elements(By.XPATH, '//*[@id="ctl00_ContentArea_ProviderSearch1_btnSearch"]')
search[0].click()
time.sleep(10)

time.sleep(5)
content = driver.page_source
#Handing over all the contents of the webpage to beautifulsoup to scrape the webpage.
soup = bs(content, 'html.parser')
# print(soup)

# soup = bs(r.text, 'html.parser')
print(soup)
print(soup.prettify())

import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from unicodedata import normalize

# table based scrapping
table_MN = pd.read_html(soup.prettify())
df = table_MN[0]
# df.head()
print(df)
time.sleep(10)
df.to_csv('data.csv', index=False)

driver.quit()


