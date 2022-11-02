import pandas as pd
import datetime as dt
from datetime import date, timedelta
from pandas.tseries.offsets import MonthEnd

i = date.today() - timedelta(months=1)
ed = date.today() - timedelta(days=1)

dates = pd.date_range(i, ed, freq='M').strftime("%Y-%m-%d")

link = "https://www.xe.com/currencytables/?from=USD&date="
fxrate = pd.concat(pd.read_html(link+d)[0].assign(Date=d) for d in dates)
newfxrate = fxrate[fxrate.Currency.isin(["AUD","CAD","CHF","EUR","GBP","INR","MXN","PHP","PEN","PLN","RMB","SGD","HKD"])]
finalfx = newfxrate[['Currency', 'Units per USD', 'USD per unit', 'Date']]

oldfx = pd.DataFrame(pd.read_csv('dailyfxrate-USD.csv'))
newfx = pd.DataFrame(finalfx)

finalfx2 = pd.concat((oldfx, newfx ),ignore_index=True).drop_duplicates().reset_index(drop=True)
finalfx2.to_csv('./dailyfxrate-USD.csv', index=False)
