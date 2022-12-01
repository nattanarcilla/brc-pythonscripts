import pandas as pd
import datetime as dt
from datetime import date, timedelta
from pandas.tseries.offsets import MonthEnd

i = date.today() - timedelta(days=15)
ed = date.today()

dates = pd.date_range(i, ed, freq='M').strftime("%Y-%m-%d")

link = "https://www.xe.com/currencytables/?from=HKD&date="
fxrate = pd.concat(pd.read_html(link+d)[0].assign(Date=d) for d in dates)
newfxrate = fxrate[fxrate.Currency.isin(["AUD","CAD","CHF","EUR","GBP","INR","MXN","PHP","PEN","PLN","CNY","SGD","NZD","USD"])]
finalfx = newfxrate[['Currency', 'Units per HKD', 'HKD per unit', 'Date']]

oldfx = pd.DataFrame(pd.read_csv('monthlyfxrate-HKD.csv')).round({"Units per HKD":3, "HKD per unit":3})
newfx = pd.DataFrame(finalfx).round({"Units per HKD":3, "HKD per unit":3})

finalfx2 = pd.concat((oldfx, newfx ),ignore_index=True).drop_duplicates().reset_index(drop=True)
finalfx2.to_csv('./monthlyfxrate-HKD.csv', index=False)
