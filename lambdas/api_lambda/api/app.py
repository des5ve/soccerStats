import json
import requests
from datetime import datetime, timedelta
from dateutil import tz
from pytz import timezone
import pymysql
import logging
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from selenium import webdriver

logger = logging.getLogger()

global browser

if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
logging.basicConfig(format='%(asctime)s %(message)s',level=logging.DEBUG)

#Leagues
prem = "https://fbref.com/en/comps/9/stats/Premier-League-Stats#stats_standard::none"
laLiga = "https://fbref.com/en/comps/12/stats/La-Liga-Stats#stats_standard::none"
ligueOne = "https://fbref.com/en/comps/13/stats/Ligue-1-Stats#stats_standard::none"
bundesliga = "https://fbref.com/en/comps/20/stats/Bundesliga-Stats#stats_standard::none"
serieA = "https://fbref.com/en/comps/11/stats/Serie-A-Stats#stats_standard::none"

#List of basic league table pages
premTable = "https://fbref.com/en/comps/9/Premier-League-Stats"
laLigaTable = "https://fbref.com/en/comps/12/La-Liga-Stats"
bundesligaTable = "https://fbref.com/en/comps/20/Bundesliga-Stats"
ligueOneTable = "https://fbref.com/en/comps/13/Ligue-1-Stats"
serieATable = "https://fbref.com/en/comps/11/Serie-A-Stats"

#load phantomJS driver
#change the executable path after you got it installed
browser = webdriver.PhantomJS(executable_path="/opt/bin/phantomjs", service_log_path='/tmp/ghostdriver.log')

def leaders(league):
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
    print(url)
    # url = "https://www.google.com"
    attempts = 0
    while (attempts < 2):
        try:
            browser.get(url)
            html = browser.page_source
            # print(html)
            soup = BeautifulSoup(html)
            all_stats_standard = soup.find_all(id='all_stats_standard')
            #print(all_stats_standard)
            players_tables = all_stats_standard[0].find_all('table')
            #print(players_tables[0])
            players = pd.read_html(str(players_tables[0]))[0]
            #print("Loaded players")
            #print(players)
            players.columns = players.columns.droplevel(0)
            #print(players.columns)
            players.columns = ['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Age', 'Born', 'MP', 'Starts', 'Min', 'Gls', 'Ast', 'PK', 'PKatt', 'CrdY', 'CrdR', 'Gls/90','Ast/90','G+A/90','G-PK/90', 'G+A-PK/90', 'xG', 'npxG', 'xA', 'xG/90', 'xA/90', 'xG+xA/90', 'npxG/90', 'npxG+xA/90', 'Matches']
            removal = players[players.xG != 'xG']
            playersClean = removal.astype(convert_dict)
            goalLeaders =  playersClean.nlargest(25, ['Gls'])
            assistLeaders = playersClean.nlargest(25, ['Ast'])
            xGLeaders = playersClean.nlargest(25, ['xG'])
            xALeaders = playersClean.nlargest(25, ['xA'])
            #print(playersClean)
            break
        except IndexError as e:
            attempts += 1
            print(attempts)
    # return (goalLeaders, assistLeaders, xGLeaders, xALeaders)
    # scorers = scores[0]

    # return "Hello World"
    return goalLeaders.to_json(orient="index")

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
    attempts = 0
    while (attempts < 5):
        try:
            browser.get(url)
            html = browser.page_source
            soup = BeautifulSoup(html)
            team_table = soup.find_all('table')
            table = pd.read_html(str(team_table[1]))[0]
            print(table)
            #cleaned_table = table.drop(["Notes"], axis=1)
            break
        except IndexError as e:
            attempts += 1
            print(attempts)
    
    return table.to_json(orient="index")
    
    # return table

def printStats(league):
    scores = leaders(league)
    teams = table(league)
    scorers = scores[0]
    #print (scorers[['Player', 'Age', 'Pos' ,'Squad', 'Gls/90', 'Ast/90', 'xG/90', 'xA/90', 'npxG/90', 'xG+xA/90']].sort_values(by = 'npxG/90', ascending=False))
    return teams.to_json(orient="index")
    # print(teams)

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    try:
        league = event['queryStringParameters']['league']
        response = leaders(league)
        # response = leaders("laLiga")
    except Exception as e:
        logger.error(e)

    return {
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,GET"
        },
        "statusCode": 200,
        "body": response
    }
