import requests
import json
from requests.auth import HTTPBasicAuth
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


frame = pd.read_csv("AllPlayers.csv")

goalLeaders = frame.query('Gls > 10')
print (goalLeaders[['Player','League', 'Squad', 'Gls/90', 'Ast/90', 'xG/90', 'xA/90', 'npxG/90', 'xG+xA/90']].sort_values(by = 'npxG/90', ascending=False))