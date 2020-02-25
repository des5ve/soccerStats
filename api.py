import requests
import json
from requests.auth import HTTPBasicAuth
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

#Leagues
prem = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F9%2Fstats%2FPremier-League-Stats&div=div_stats_standard"
laLiga = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F12%2Fstats%2FLa-Liga-Stats&div=div_stats_standard"
ligueOne = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F13%2Fstats%2FLigue-1-Stats&div=div_stats_standard"
bundesliga = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F20%2Fstats%2FBundesliga-Stats&div=div_stats_standard"
serieA = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F11%2Fstats%2FSerie-A-Stats&div=div_stats_standard"

#Convert Dataframe Colunns to proper Datatypes
convert_dict = {'Min': float,
                'Gls': float, 
                'Ast': float,
                'PK': float,
                'PKatt': float,
                'CrdY': float,
                'CrdR': float,
                'Gls/90': float,
                'Ast/90': float,
                'G+A/90': float,
                'G-PK/90': float,
                'G+A-PK/90': float,
                'xG': float,
                'npxG': float,
                'xA': float,
                'xG/90': float,
                'xA/90': float,
                'xG+xA/90': float,
                'npxG/90': float}



def leaders(league):
    if league == "epl":
        url = prem
    elif league == 'bundesliga':
        url = bundesliga
    elif league == 'laLiga':
        url = laLiga
    elif league == 'serieA':
        url = serieA
    elif league == 'ligueOne':
        url = ligueOne
    else:
        print ("League Not Recognized. Options are: epl, bundesliga, laLiga, serieA, ligueOne") 
    players = pd.read_html(url, encoding='utf8')[0] 
    players.columns = players.columns.droplevel(0)
    players.columns = ['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Age', 'Born', 'MP', 'Starts', 'Min', 'Gls', 'Ast', 'PK', 'PKatt', 'CrdY', 'CrdR', 'Gls/90','Ast/90','G+A/90','G-PK/90', 'G+A-PK/90', 'xG', 'npxG', 'xA', 'xG/90', 'xA/90', 'xG+xA/90', 'npxG/90', 'npxG+xA/90', 'Matches']
    removal = players[players.xG != 'xG']
    playersClean = removal.astype(convert_dict)
    goalLeaders =  playersClean.nlargest(25, ['Gls'])
    assistLeaders = playersClean.nlargest(25, ['Ast'])
    xGLeaders = playersClean.nlargest(25, ['xG'])
    xALeaders = playersClean.nlargest(25, ['xA'])
    return (goalLeaders, assistLeaders, xGLeaders, xALeaders)



eplScorers = leaders("epl")
bundesligaScorers = leaders("bundesliga")
serieAScorers = leaders("serieA")
laLigaScorers = leaders("laLiga")
ligueOneScorers = leaders("ligueOne")


