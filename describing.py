df =  yfinance.download("TSLA", start, end) #Need yfiance
df["Factor"] = df["Close"] / df["Adj Close"]
print(df["Factor"].nunique(), df["Factor"].count())
