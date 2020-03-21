import requests
import json
from requests.auth import HTTPBasicAuth
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import urllib

#Leagues
# prem = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F9%2Fstats%2FPremier-League-Stats&div=div_stats_standard"
# laLiga = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F12%2Fstats%2FLa-Liga-Stats&div=div_stats_standard"
# ligueOne = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F13%2Fstats%2FLigue-1-Stats&div=div_stats_standard"
# bundesliga = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F20%2Fstats%2FBundesliga-Stats&div=div_stats_standard"
# serieA = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F11%2Fstats%2FSerie-A-Stats&div=div_stats_standard"

#Leagues
prem = "https://fbref.com/stathead/share.fcgi?id=/DHQKM&lang=en"
laLiga = "https://fbref.com/stathead/share.fcgi?id=/Wh2eo&lang=en"
ligueOne = ""
bundesliga = "https://fbref.com/stathead/share.fcgi?id=/W4BCU&lang=en"
serieA = "https://fbref.com/stathead/share.fcgi?id=/vjuJk&lang=en"

#List of basic League Table Widgets
# premTable = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F9%2FPremier-League-Stats&div=div_results32321_overall"
# laLigaTable = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F12%2FLa-Liga-Stats&div=div_results32391_overall"
# bundesligaTable = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F20%2FBundesliga-Stats&div=div_results32481_overall"
# ligueOneTable = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F13%2FLigue-1-Stats&div=div_results32431_overall"
# serieATable = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F11%2FSerie-A-Stats&div=div_results32601_overall"

#List of basic league table pages
premTable = "https://fbref.com/en/comps/9/Premier-League-Stats"
laLigaTable = "https://fbref.com/en/comps/12/La-Liga-Stats"
bundesligaTable = "https://fbref.com/en/comps/20/Bundesliga-Stats"
ligueOneTable = "https://fbref.com/en/comps/13/Ligue-1-Stats"
serieATable = "https://fbref.com/en/comps/11/Serie-A-Stats"

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
    # print(url)
    if url:
        r = requests.get(url, headers={"User-Agent":"Mozilla/5.0"})
        soup = BeautifulSoup(r.text)
        # print(r.encoding)
        all_stats_standard = soup.find_all('table')
        # print(all_stats_standard)
        players = pd.read_html(str(all_stats_standard))[0]
        # players.columns = players.columns.droplevel(0)
        print(players.columns)
        players.columns = ['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Age', 'Born', 'MP', 'Starts', 'Min', 'Gls', 'Ast', 'PK', 'PKatt', 'CrdY', 'CrdR', 'Gls/90','Ast/90','G+A/90','G-PK/90', 'G+A-PK/90', 'xG', 'npxG', 'xA', 'xG/90', 'xA/90', 'xG+xA/90', 'npxG/90', 'npxG+xA/90', 'Matches']
        removal = players[players.xG != 'xG']
        playersClean = removal.astype(convert_dict)
        goalLeaders =  playersClean.nlargest(25, ['Gls'])
        assistLeaders = playersClean.nlargest(25, ['Ast'])
        xGLeaders = playersClean.nlargest(25, ['xG'])
        xALeaders = playersClean.nlargest(25, ['xA'])
        return (goalLeaders, assistLeaders, xGLeaders, xALeaders)


def table(league):
    if league == "epl":
        url = premTable
    elif league == 'bundesliga':
        url = bundesligaTable
    elif league == 'laLiga':
        url = laLigaTable
    elif league == 'serieA':
        url = serieATable
    elif league == 'ligueOne':
        url = ligueOneTable
    else:
        print ("League Not Recognized. Options are: epl, bundesliga, laLiga, serieA, ligueOne")
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    all_stats_standard = soup.find_all('table')
    table = pd.read_html(str(all_stats_standard))[0]
    return table

def printStats(league):
    scores = leaders(league)
    teams = table(league)
    if scores:
        scorers = scores[0]
        print (scorers[['Player', 'Age', 'Pos' ,'Squad', 'Gls/90', 'Ast/90', 'xG/90', 'xA/90', 'npxG/90', 'xG+xA/90']].sort_values(by = 'npxG/90', ascending=False))
    if not teams.empty:
        print (teams)

printStats("epl")

# eplScorers = leaders("epl")
# bundesligaScorers = leaders("bundesliga")
# serieAScorers = leaders("serieA")
# laLigaScorers = leaders("laLiga")
# ligueOneScorers = leaders("ligueOne")

# eplT = table("epl")
# bundesligaT = table("bundesliga")
# serieAT = table("serieA")
# laLigaT = table("laLiga")
# ligueOneT = table("ligueOne")

