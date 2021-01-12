# Install requests: pip install requests
import requests
# Install BeautifulSoup: pip install BeautifulSoup4
from bs4 import BeautifulSoup
# Install pandas: pip install pandas
import pandas as pd

#data collected from forcast.weather.gov
url = str(input('Paste URL from "forcast.weather.gov" : '))

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

week = soup.find(id = "seven-day-forecast-body")

items = week.find_all(class_ = 'tombstone-container')

period_names = [period.find(class_='period-name').get_text() for period in items]

short_descriptions = [short.find(class_='short-desc').get_text() for short in items]

temperatures = [temp.find(class_='temp').get_text() for temp in items]

weather_stuff = pd.DataFrame(
    {'period': period_names,
     'short_descriptions': short_descriptions,
     'temperatures': temperatures,
     })

name = str(input("Enter Name of CSV file : "))

save_name = name+".csv"

weather_stuff.to_csv(save_name)