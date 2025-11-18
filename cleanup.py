#scrape and cleanup box office data

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from bs4 import BeautifulSoup
import requests
from datetime import date

# Request to website and download HTML contents
url='https://www.boxofficemojo.com/month/by-year/2021/'

req=requests.get(url)
content=req.text

# Beautiful Soup
soup=BeautifulSoup(content, features = "html.parser")

rows =  soup.findAll('tr')
print(rows)
data = rows[8].findAll('td')
# print(data)

# Date when tthere is a special occasion listed
# print('-----------------')
# print(data[0].findAll('a')[0].text)
# # special occasion
# print('-----------------')
# print(data[0].findAll('span')[0].text)

def scraper(year):
    url=f'https://www.boxofficemojo.com/weekend/by-year/{year}/'
    req=requests.get(url)
    content=req.text
    soup=BeautifulSoup(content)
    rows=soup.findAll('tr')
    appended_data = []
    for row in rows:
        data_row = {}
        data = row.findAll('td')
        if len(data) == 0:
            continue
        if len(data[0].findAll('span')) > 0:
        #special weekend
            data_row['occasion'] = data[0].findAll('span')[0].text
            data_row['date'] = data[0].findAll('a')[0].text
        else:
        #normal weekend
            data_row['occasion'] = ""
            data_row['date'] = data[0].text
        data_row['top10_gross'] = data[1].text
        data_row['top10_wow_change'] = data[2].text
        data_row['overall_gross'] = data[3].text
        data_row['overall_wow_change'] = data[4].text
        data_row['num_releases'] = data[5].text
        data_row['top_release'] = data[6].text
        data_row['week_no'] = data[10].text
        appended_data.append(data_row)
    weekend_data = pd.DataFrame(appended_data, columns = ['date', 'occasion', 'top10_gross', 'top10_wow_change', 'overall_gross', 'overall_wow_change', 'num_releases', 'top_release', 'week_no'])
    weekend_data.to_csv(f'./data/weekend_summary_{year}.csv', index=False)

todays_date = date.today()
current_year = todays_date.year

years = range(1977, current_year+1)

def clean():
    for year in years:
        scraper(year)
        
print(clean())

    



