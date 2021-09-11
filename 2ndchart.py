ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan = 1 )
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan = 1)

df["100ma"]= df["Adj Close"].rolling(window=100).mean()
df.dropna(inplace = True)
print(df.head())
ax1.plot(df.index,df["Adj Close"])
ax1.plot(df.index,df["100ma"])
ax2.plot(df.index,df["100ma"])
plt.show
