import requests
import json
from requests.auth import HTTPBasicAuth
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


frame = pd.read_csv("AllPlayers.csv")

#print (goalLeaders[['Player','League', 'Squad', 'Gls/90', 'Ast/90', 'xG/90', 'xA/90', 'npxG/90', 'xG+xA/90']].sort_values(by = 'npxG/90', ascending=False))



def plotGoalLeaders():
    goalLeaders = frame.query('Gls > 7')
    x = goalLeaders['xG']
    y = goalLeaders['Gls']
    plt.plot(x,y, 'ro')
    plt.axis([0,30,0,30])
    plt.ylabel('Goals')
    plt.xlabel('Expected Goals')
    plt.show()


epl = frame[(frame.League == 'epl') & (frame.Gls > 7 )]
bundesliga = frame[(frame.League == 'bundesliga') & (frame.Gls > 7 )]
ligueOne = frame[(frame.League == 'ligueOne') & (frame.Gls > 7 )]
x = epl['xG']
y = epl['Gls']
x1 = bundesliga['xG']
y1 = bundesliga['Gls']
x2 = ligueOne['xG']
y2 = ligueOne['Gls']

plt.figure(figsize=(15, 5))
plt.subplot(131)
plt.scatter(x,y)
plt.subplot(132)
plt.scatter(x1, y1)
plt.subplot(133)
plt.scatter(x2, y2)
plt.suptitle('Expected Goals vs Goals')
plt.show()


"""coef = np.polyfit(x,y,1)
poly1d_fn = np.poly1d(coef) 
plt.plot(x,y, 'yo', x, poly1d_fn(x), '--k')"""

