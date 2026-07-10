# pip install mplfinance 
import mplfinance as mpl 
import pandas as pd 
#load data 
nifty = pd.read_csv('nifty50.csv').squeeze()
nifty["Date"] = pd.to_datetime(nifty["Date"])
nifty.set_index('Date', inplace=True)
mpl.plot(nifty,type='candle',title='Nifty 50',style='yahoo')
