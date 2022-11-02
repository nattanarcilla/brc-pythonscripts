#import json
import pandas as pd
import datetime as dt
from datetime import date, timedelta

delta = dt.timedelta(days=1)
i = date.today() - timedelta(days=5)
ed = date.today() - timedelta(days=1)

dates = []

while i <= ed:
    dates.append(str(i))
    i += delta

link = "https://www.xe.com/currencytables/?from=USD&date="
webrate = pd.concat(pd.read_html(link+d)[0].assign(Date=d) for d in dates)
filteredratexrate = webrate[webrate.Currency.isin(["AUD","CAD","CHF","EUR","GBP","INR","MXN","PHP","PEN","PLN","RMB","SGD","HKD"])]
fxrate = filteredratexrate[['Currency', 'Units per USD', 'USD per unit', 'Date']]

#load current exchange rate file and merge with new exchange rate
#oldfx = pd.DataFrame(json.load(open('dailyfxrate-USD.json')))
oldfx = pd.DataFrame(pd.read_csv('dailyfxrate-USD.csv'))
newfx = pd.DataFrame(fxrate)

finalfx = pd.concat((oldfx, newfx ),ignore_index=True).drop_duplicates().reset_index(drop=True)
#finalfx.to_json('./dailyfxrate-USD.json', orient='records', indent=2)
finalfx.to_csv('./dailyfxrate-USD.csv', index=False)
