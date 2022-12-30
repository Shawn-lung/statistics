import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import datetime

def setmonth(month):
    return(month)    

liststock = ['^DJI','^FTSE','^N225','000001.SS','^KS11','^GDAXI','^FCHI','^JKSE','^BSESN','^KLSE','^STI','PSEI.PS']
name = ['USA','UK','JP','CN','KR','DE','FR','ID','IN','MY','SG','PH']

for n in range (len(liststock)):
    monthlyreturn = []
    month = []
    color1 = []
    dfavg = []
    xvalue = []
    df=yf.download(tickers=liststock[n],interval = '1mo',start='2018-12-01',end=datetime.datetime.now())
    df = df.dropna()
    df['Return'] = (df['Adj Close']/df['Adj Close'].shift(1))-1
    df = df.dropna()
    df['Month'] = df.index.month
    df['Month'] = df['Month'].apply(setmonth)  
    dfdec = df[df['Month'] == 12]
    df = df.drop(index = df.loc[df['Month'] == 12].index)
    df['Year'] = df.index.year
    for i in df['Year'].unique():
        dfavg.append(df[df['Year'] == i]['Return'].mean())
    for i in range(len(dfdec)-len(dfavg)):
        dfdec=dfdec.drop(index = dfdec.tail(1).index)
    print(dfavg)
    print(dfdec['Return'])
    years = dfdec.index.year
    ax = plt.subplot(3,4,n+1)
    x = np.arange(len(years))
    width = 0.4
    print(x)
    ax.set_title(name[n])
    ax.set_xticks(x, years)
    ax.bar(x+width/2,height=dfdec['Return'],color = 'red',width=width,label='Dec')
    ax.bar(x-width/2,height=dfavg,width=width)
    axes = plt.gca()
    axes.xaxis.set_major_locator(dates.DayLocator(interval=2))

plt.show()