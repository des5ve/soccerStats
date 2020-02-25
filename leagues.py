import requests
import json
from requests.auth import HTTPBasicAuth
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

prem = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F9%2FPremier-League-Stats&div=div_results32321_overall"
laLiga = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F12%2FLa-Liga-Stats&div=div_results32391_overall"
bundesliga = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F20%2FBundesliga-Stats&div=div_results32481_overall"
ligueOne = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F13%2FLigue-1-Stats&div=div_results32431_overall"
serieA = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F11%2FSerie-A-Stats&div=div_results32601_overall"

table = pd.read_html(prem, encoding='utf8')[0]



def leagueTable(league):
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
    league = pd.read_html(url)
    print (league)



