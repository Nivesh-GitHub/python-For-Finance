
df["SMA1"] = df['Close'].rolling(window=50).mean()
df["SMA2"] = df['Close'].rolling(window=200).mean()

plt.figure(figsize=(10,10))
plt.plot(df['SMA1'], 'g--', label="SMA1")
plt.plot(df['SMA2'], 'r--', label="SMA2")
plt.plot(df['Close'], label="Close")
plt.legend()
plt.show()
