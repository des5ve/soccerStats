import requests
import json
from requests.auth import HTTPBasicAuth
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs")

url = "https://fbref.com/en/players/d5dd5f1f/matchlogs/2020-2021/summary/Pierre-Emerick-Aubameyang-Match-Logs"

attempts = 0
while (attempts < 2):
    try:
        browser.get(url)
        html = browser.page_source
        #print(html)
        soup = BeautifulSoup(html)
        all_stats_standard = soup.find_all(id='div_matchlogs_all')
        #print(all_stats_standard)
        players_tables = all_stats_standard[0].find_all('table')
        #print(players_tables[0])
        stats = pd.read_html(str(players_tables[0]))[0]
        print (stats)
        #print("Loaded players")
        #print(players)
        stats.columns = stats.columns.droplevel(0)
        print(stats)     
        break
    except IndexError as e:
        attempts += 1
        print(attempts)
