import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import datetime

class Data:
    def __init__(self,name,year,month):
        self.name = name
        self.month = month
        self.date = self.set_date(year,month)
        self.data = []
        self.sub = []
    
    def set_date(self,year,month):
        self.years = int((datetime.datetime.now()-pd.Timestamp(year+'-'+month+'-01')).days/365.25)+1
        return(pd.Timestamp(year+'-'+month+'-01'))
    
    def get_data(self):
        for i in range(self.years):
            start_date = self.date+pd.DateOffset(years=i)
            end_date = start_date+pd.DateOffset(months=12-int(self.month)+1)
            if end_date > datetime.datetime.now():
                end_date = datetime.datetime.now()
            self.data.append(yf.download(self.name, start=start_date, end=end_date))
        self.dimension()
        self.draw_data()
    
    def dimension(self):
        for i in range(1,self.years+1):
            if self.years%i == 0:
                self.sub.append(i)
        if len(self.sub)%2 == 0:
            self.sub = self.sub[int(len(self.sub)/2-1):int(len(self.sub)/2+1)]
        else:
            self.sub = [self.sub[int(len(self.sub)/2)]] 
            self.sub.append(self.sub[0])
    
    def draw_data(self):
        for i in range(self.years):
            plt.subplot(self.sub[1],self.sub[0],i+1)
            plt.plot(self.data[i]['Adj Close'])
            axes = plt.gca()
            axes.xaxis.set_major_locator(dates.DayLocator(interval=8*(12-int(self.month)+1)))
        plt.show()
        

