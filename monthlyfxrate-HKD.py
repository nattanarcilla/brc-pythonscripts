#import json
import pandas as pd
import datetime as dt
from datetime import date, timedelta
from pandas.tseries.offsets import MonthEnd

i = dt.date(2022, 1, 1)
ed = date.today()

dates = pd.date_range(i, ed, freq='BM').strftime("%Y-%m-%d")

link = "https://www.xe.com/currencytables/?from=HKD&date="
fxrate = pd.concat(pd.read_html(link+d)[0].assign(Date=d) for d in dates)
newfxrate = fxrate[fxrate.Currency.isin(["AUD","CAD","CHF","EUR","GBP","INR","MXN","PHP","PEN","PLN","RMB","SGD","USD"])]
finalfx = newfxrate[['Currency', 'Units per HKD', 'HKD per unit', 'Date']]

#finalfx.to_json('./monthlyfxrate-HKD.json', orient='records', indent=2)
finalfx.to_csv('./monthlyfxrate-HKD.csv', index=False)
