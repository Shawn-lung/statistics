import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def setmonth(month):
    if month == 1:
        return(12)
    else:
        return(month-1)    

def p_or_m(value):
    if value <= 0:
        return 0
    else:
        return 1


monthlyp = []
month = []
color1 = []

df = yf.download(tickers='SPY',period='max',interval = '1mo')
df = df.dropna()
df['Return'] = (df['Adj Close']/df['Adj Close'].shift(1))-1
df = df.dropna()
df['Month'] = df.index.month
df['Month'] = df['Month'].apply(setmonth)
df['PlusorMinus'] = df['Return'].apply(p_or_m)
print(df)
for i in range(12):
    monthlyp.append(df[df['Month'] == i+1]['PlusorMinus'].mean())
    month.append(str(i+1))

plt.bar(x=month,height=monthlyp)
plt.show()