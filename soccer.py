import requests
import json
from requests.auth import HTTPBasicAuth
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import teamDictionary




#Premier League Table
premURL = "https://fbref.com/en/comps/9/Premier-League-Stats"
premTable = pd.read_html(premURL)[0]

#La Liga Table
laLigaUrl = "https://fbref.com/en/comps/12/La-Liga-Stats"
laLigaTable = pd.read_html(laLigaUrl)[0]

#Ligue 1 Table
ligueOneUrl = "https://fbref.com/en/comps/13/Ligue-1-Stats"
ligueOneTable = pd.read_html(ligueOneUrl)[0]

#Bundesliga Table
bundesligaUrl = "https://fbref.com/en/comps/20/Bundesliga-Stats"
bundesligaTable = pd.read_html(bundesligaUrl)[0]

#Serie A Table
serieAUrl = "https://fbref.com/en/comps/11/Serie-A-Stats"
serieATable = pd.read_html(serieAUrl)[0]




"""
#Arsenal
urlA = "https://fbref.com/en/squads/18bb7c10/Arsenal"
response = requests.get(urlA)
soup = BeautifulSoup(response.content, 'html5lib')
#All Competition Stats
ArsenalSeason = pd.read_html(urlA)[4]
#Remove Top Level of Panda Index
ArsenalSeason.columns = ArsenalSeason.columns.droplevel(0)
#Queries for Stats
epl = ArsenalSeason.query('xG > .25')
print (epl[['Player', 'xG', 'Gls']] )
df2 = epl.rename(columns={epl.columns[25]: 'npxG+xA/90'})
print('df2')
print (df2)
"""


"""
for url in teamDictionary.values():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')
    seasonStats = pd.read_html(url)[4]
    seasonStats.columns = seasonStats.columns.droplevel(0)
    xGLeaders = seasonStats.query('xG > .25')
    print (xGLeaders[['Player', 'xG', 'Gls']])
"""   