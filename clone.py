import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import datetime

class Data:
    def __init__(self,name,year):
        self.name = name
        self.date = self.set_date(year)
        self.data = []
        self.sub = []
    
    def set_date(self,year):
        self.years = int((datetime.datetime.now()-pd.Timestamp(year+'-12-01')).days/365)+1
        return(pd.Timestamp(year+'-12-01'))
    
    def get_data(self):
        for i in range(self.years):
            start_date = self.date+pd.DateOffset(years=i)
            print(start_date) 
            end_date = start_date+pd.DateOffset(months=1)
            if end_date > datetime.datetime.now():
                end_date = datetime.datetime.now()
            print(end_date)
            self.data.append(yf.download(self.name, start=start_date, end=end_date))
        self.dimension()
        self.draw_data()
    
    def dimension(self):
        for i in range(1,self.years+1):
            if self.years%i == 0:
                print(i)
                self.sub.append(i)
        print(self.sub)
        if len(self.sub)%2 == 0:
            self.sub = self.sub[int(len(self.sub)/2-1):int(len(self.sub)/2+1)]
            print(self.sub)
        else:
            self.sub = [self.sub[int(len(self.sub)/2)]] 
            self.sub.append(self.sub[0])
            print(self.sub)
    
    def draw_data(self):
        for i in range(self.years):
            plt.subplot(self.sub[1],self.sub[0],i+1)
            plt.plot(self.data[i]['Adj Close'])
            axes = plt.gca()
            axes.xaxis.set_major_locator(dates.DayLocator(interval=10))
        plt.show()
        

