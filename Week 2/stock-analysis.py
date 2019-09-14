import pandas as pd
import datetime
import pandas_datareader.data as web

start = datetime.datetime(2010,1,1)
end = datetime.datetime(2017,1,11)

df = web.DataReader("AAPL",'yahoo',start,end)
df.tail