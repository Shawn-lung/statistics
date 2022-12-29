import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def setmonth(month):
    if month == 1:
        return(12)
    else:
        return(month-1)    

monthlyreturn = []
month = []

df = yf.download(tickers='SPY',period='max',interval = '1mo')
df = df.dropna()
df['Return'] = (df['Adj Close']/df['Adj Close'].shift(1))-1
df = df.dropna()
df['Month'] = df.index.month
df['Month'] = df['Month'].apply(setmonth)
print(df.head(30))
for i in range(12):
    monthlyreturn.append(df[df['Month'] == i+1]['Return'].mean())
    month.append(str(i+1))
plt.bar(x=month,height=monthlyreturn)
plt.show()