import requests
import json
from requests.auth import HTTPBasicAuth
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import urllib
from sqlalchemy import create_engine as ce
from selenium import webdriver

#load phantomJS driver
browser = webdriver.PhantomJS(executable_path="C:\\Users\\Shashank\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")

premTable = "https://fbref.com/en/comps/9/Premier-League-Stats"
laLigaTable = "https://fbref.com/en/comps/12/La-Liga-Stats"
bundesligaTable = "https://fbref.com/en/comps/20/Bundesliga-Stats"
ligueOneTable = "https://fbref.com/en/comps/13/Ligue-1-Stats"
serieATable = "https://fbref.com/en/comps/11/Serie-A-Stats"

# create sqlalchemy engine
engine = ce("mysql+pymysql://{user}:{pw}@/{db}"
                       .format(user="",
                               pw="",
                               db=""))

def loadTable(league):
    if league == "epl":
        url = premTable
        tableName = "premTeamTable"
    elif league == 'bundesliga':
        url = bundesligaTable
        tableName = "bundesligaTeamTable"
    elif league == 'laLiga':
        url = laLigaTable
        tableName = "laligaTeamTable"
    elif league == 'serieA':
        url = serieATable
        tableName = "serieATeamTable"
    elif league == 'ligueOne':
        url = ligueOneTable
        tableName = "ligueOneTeamTable"
    else:
        print ("League Not Recognized. Options are: epl, bundesliga, laLiga, serieA, ligueOne")
    attempts = 0
    while (attempts < 5):
        try:
            browser.get(url)
            html = browser.page_source
            soup = BeautifulSoup(html)
            team_table = soup.find_all('table')
    #         print(team_table[1])
            table = pd.read_html(str(team_table[0]))[0]
            # print(table)
            cleaned_team_df = table.drop(["Notes"], axis=1)
            print(cleaned_team_df)
            cleaned_team_df.to_sql(tableName, con = engine, if_exists = 'replace', index=False, chunksize = 1000)
            print("Inserted table for league "+league)
            break
        except IndexError as e:
            attempts += 1
            print(attempts)
    

loadTable("serieA")
