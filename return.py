import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import datetime

def setmonth(month):
        return(month)    

liststock = ['^DJI','^FTSE','^N225','000001.SS','^KS11','^GDAXI','^FCHI','^JKSE','^BSESN','^KLSE','^STI','PSEI.PS']
name = ['USA','UK','JP','CN','KR','DE','FR','ID','IN','MY','SG','PH']

for n in range (len(liststock)):
    monthlyreturn = []
    month = []
    color1 = []

    df=yf.download(tickers=liststock[n],interval = '1mo',start='1950-12-01',end=datetime.datetime.now())
    df = df.dropna()
    df['Return'] = (df['Adj Close']/df['Adj Close'].shift(1))-1
    df = df.dropna()
    df['Month'] = df.index.month
    df['Month'] = df['Month'].apply(setmonth)
    if name[n]=='USA':    
        print(df[df['Month'] == 11])
        print(df[df['Month'] == 12])

    for i in range(12):
        monthlyreturn.append(df[df['Month'] == i+1]['Return'].mean())
        month.append(str(i+1))
        if i == 11:
            color1.append('blue')
        elif df[df['Month'] == i+1]['Return'].mean() > 0 :
            color1.append('red')
        else:
            color1.append('green')
    plt.subplot(3,4,n+1)
    plt.title(name[n])
    plt.bar(x=month,height=monthlyreturn,color = color1)
plt.show()