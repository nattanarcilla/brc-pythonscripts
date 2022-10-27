import json
import pandas as pd
import datetime as dt
from datetime import date

delta = dt.timedelta(days=1)
i = dt.date(date.today().year, date.today().month, date.today().day -5)
ed = dt.date(date.today().year, date.today().month, date.today().day -1)

dates = []

while i <= ed:
    dates.append(str(i))
    i += delta

link = "https://www.xe.com/currencytables/?from=USD&date="
webrate = pd.concat(pd.read_html(link+d)[0].assign(Date=d) for d in dates)
filteredratexrate = webrate[webrate.Currency.isin(["AUD","CAD","CHF","EUR","GBP","INR","MXN","PHP","PEN","PLN","RMB","SGD","HKD"])]
fxrate = filteredratexrate[['Currency', 'Units per USD', 'USD per unit', 'Date']]

#load current exchange rate file and merge with new exchange rate
oldfx = pd.DataFrame(json.load(open('dailyfxrate-USD.json')))
newfx = pd.DataFrame(fxrate)

finalfx = pd.concat((oldfx, newfx ), axis = 0).drop_duplicates(subset=['Currency', 'Units per USD', 'USD per unit', 'Date'], keep=‘first’).reset_index(drop=True)

finalfx.to_json('./dailyfxrate-USD.json', orient='records', indent=2)
