# pip install mplfinance 
import mplfinance as mpl 
import pandas as pd 

#load data 
nifty = pd.read_csv('nifty50.csv').squeeze()
print(nifty)