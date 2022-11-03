import pandas as pd
import datetime as dt
from datetime import date, timedelta

delta = dt.timedelta(days=1)
i = date.today() - timedelta(days=2)
ed = date.today()

dates = []

while i <= ed:
    dates.append(str(i))
    i += delta

link = "https://www.xe.com/currencytables/?from=HKD&date="
webrate = pd.concat(pd.read_html(link+d)[0].assign(Date=d) for d in dates)
filteredratexrate = webrate[webrate.Currency.isin(["AUD","CAD","CHF","EUR","GBP","INR","MXN","PHP","PEN","PLN","RMB","SGD","USD"])]
fxrate = filteredratexrate[['Currency', 'Units per HKD', 'HKD per unit', 'Date']]

oldfx = pd.DataFrame(pd.read_csv('dailyfxrate-HKD.csv'))
newfx = pd.DataFrame(fxrate)

finalfx = pd.concat((oldfx, newfx ),ignore_index=True).drop_duplicates().reset_index(drop=True)

finalfx.to_csv('./dailyfxrate-HKD.csv', index=False)
