import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

class Data:
    def __init__(self,name):
        self.name = name
    def get_data(self):
        self.data1 = yf.download(self.name, start="2017-12-01", end="2017-12-31" )
        self.data2 = yf.download(self.name, start="2018-12-01", end="2018-12-31" )
        self.data3 = yf.download(self.name, start="2019-12-01", end="2019-12-31" )
        self.data4 = yf.download(self.name, start="2020-12-01", end="2020-12-31" )
        self.data5 = yf.download(self.name, start="2021-12-01", end="2021-12-31" )
        self.data6 = yf.download(self.name, start="2022-12-01", end="2022-12-20" )
        self.draw_data()
    def draw_data(self):
        plt.subplot(3, 2, 1)
        plt.plot(self.data1['Adj Close'])
        plt.title("2017", {'fontsize':15}) 
        plt.subplot(3, 2, 2)
        plt.plot(self.data2['Adj Close'])
        plt.title("2018", {'fontsize':15}) 
        plt.subplot(3, 2, 3)
        plt.plot(self.data3['Adj Close'])
        plt.title("2019", {'fontsize':15}) 
        plt.subplot(3, 2, 4)
        plt.plot(self.data4['Adj Close'])
        plt.title("2020", {'fontsize':15}) 
        plt.subplot(3, 2, 5)
        plt.plot(self.data5['Adj Close'])
        plt.title("2021", {'fontsize':15}) 
        plt.subplot(3, 2, 6)
        plt.plot(self.data6['Adj Close'])
        plt.title("2022", {'fontsize':15}) 
        plt.show()

