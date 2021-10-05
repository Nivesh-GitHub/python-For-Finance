import datetime as dt
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import yfinance as yfinance
from matplotlib.pyplot import subplot2grid
import os




start = dt.datetime(2000,1,1)
end = dt.datetime(2021,12,31)





df=  yfinance.download("FORCEMOT.BO", start, end) #Need yfiance
df["Factor"] = df["Close"] / df["Adj Close"]
print(df["Factor"].unique(), df["Factor"].count())





print(df.head())





df_ohlc = df["Adj Close"].resample("10D").ohlc()
df_volume = df["Volume"].resample("10D").sum()
print(df_ohlc.head())






df["SMA1"] = df['Close'].rolling(window=50).mean()
df["SMA2"] = df['Close'].rolling(window=200).mean()

plt.figure(figsize=(10,10))
plt.plot(df['SMA1'], 'g--', label="SMA1")
plt.plot(df['SMA2'], 'r--', label="SMA2")
plt.plot(df['Close'], label="Close")
plt.legend()
plt.show()






  
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan = 1 )
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan = 1)

df["100ma"]= df["Adj Close"].rolling(window=100).mean()
df.dropna(inplace = True)
print(df.head())
ax1.plot(df.index,df["Adj Close"])
ax1.plot(df.index,df["100ma"])
ax2.plot(df.index,df["100ma"])
plt.show





  
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan = 1 )
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan = 1,sharex =ax1)
df_ohlc = df["Adj Close"].resample("10D").mean()
df["100ma"]= df["Adj Close"].rolling(window=100).sum()

df_volume = df["Volume"].resample("10D").sum #days is d
df.dropna(inplace = True)
print(df.head())
ax1.plot(df.index,df["Adj Close"])#Close of market
ax1.plot(df.index,df["100ma"])
ax2.plot(df.index,df["100ma"]) #ma stands for moving average
plt.show

#Thank you 
