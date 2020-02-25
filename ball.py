import requests
import json
from requests.auth import HTTPBasicAuth
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

url = "https://basketball.realgm.com/international/boxscore/2020-01-05/Pallacanestro-Trieste-2004-at-Consultinvest-VL-Pesaro/351539"
df = pd.read_html(url)[3]
print (df)