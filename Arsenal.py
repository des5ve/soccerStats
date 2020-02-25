import requests
import json
from requests.auth import HTTPBasicAuth
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import statsmodels.api as sm


urlA = "https://fbref.com/en/squads/18bb7c10/Arsenal#all_ks_sched_all"
schedule = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F18bb7c10%2FArsenal&div=div_ks_sched_all"
response = requests.get(urlA)
soup = BeautifulSoup(response.content, 'html5lib')
#All Competition Stats
allComp = pd.read_html(urlA)[4]
#EPL Season
epl = pd.read_html(urlA)[0]
#Remove Top Level of Panda Index
allComp.columns = allComp.columns.droplevel(0)
epl.columns = epl.columns.droplevel(0)
#Renaming Of Dataframe

epl.columns = ['Player', 'Nation', 'Pos', 'Age', 'MP', 'Starts', 'Min', 'Gls', 'Ast', 'Pk', 'PKatt', 'CrdY', 'CrdR', 'Gls/90','Ast/90','G+A/90','G-PK/90', 'G+A-PK/90', 'xG', 'npxG', 'xA', 'xG/90', 'xA/90', 'xG+xA/90', 'npxG/90', 'npxG+xA/90', 'Matches']
allComp.columns = ['Player', 'Nation', 'Pos', 'Age', 'MP', 'Starts', 'Min', 'Gls', 'Ast', 'Pk', 'PKatt', 'CrdY', 'CrdR', 'Gls/90','Ast/90','G+A/90','G-PK/90', 'G+A-PK/90', 'xG', 'npxG', 'xA', 'xG/90', 'xA/90', 'xG+xA/90', 'npxG/90', 'npxG+xA/90', 'Matches']

print (allComp)
arsenal = pd.read_html(schedule)[0]
print (arsenal)
