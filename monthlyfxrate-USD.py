#import json
import pandas as pd
import datetime as dt
from datetime import date
from pandas.tseries.offsets import MonthEnd

i = dt.date(2022, 1, 1)
ed = dt.date(date.today().year, date.today().month, date.today().day -1)

dates = pd.date_range(i, ed, freq='BM').strftime("%Y-%m-%d")

link = "https://www.xe.com/currencytables/?from=USD&date="
fxrate = pd.concat(pd.read_html(link+d)[0].assign(Date=d) for d in dates)
newfxrate = fxrate[fxrate.Currency.isin(["AUD","CAD","CHF","EUR","GBP","INR","MXN","PHP","PEN","PLN","RMB","SGD","HKD"])]
finalfx = newfxrate[['Currency', 'Units per USD', 'USD per unit', 'Date']]

#finalfx.to_json('./monthlyfxrate-USD.json', orient='records', indent=2)
finalfx.to_csv('./monthlyfxrate-USD.csv', index=False)
