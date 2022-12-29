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
color1 = []

df = yf.download(tickers='SPY',period='max',interval = '1mo')
df = df.dropna()
df['Return'] = (df['Adj Close']/df['Adj Close'].shift(1))-1
df = df.dropna()
df['Month'] = df.index.month
df['Month'] = df['Month'].apply(setmonth)

for i in range(12):
    monthlyreturn.append(df[df['Month'] == i+1]['Return'].mean())
    month.append(str(i+1))
    if i == 11:
        color1.append('blue')
    elif df[df['Month'] == i+1]['Return'].mean() > 0 :
        color1.append('red')
    else:
        color1.append('green')
plt.bar(x=month,height=monthlyreturn,color = color1)
plt.show()