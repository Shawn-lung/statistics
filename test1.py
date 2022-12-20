import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

print(pd.to_datetime('20211011')+pd.DateOffset(years=1))

data1 = yf.download("^DJI", start="2017-12-01", end="2017-12-31" )
data2 = yf.download("^DJI", start="2018-12-01", end="2018-12-31" )
data3 = yf.download("^DJI", start="2019-12-01", end="2019-12-31" )
data4 = yf.download("^DJI", start="2020-12-01", end="2020-12-31" )
data5 = yf.download("^DJI", start=pd.to_datetime('20211011'),end = pd.to_datetime('20211231') )
data6 = yf.download("^DJI", start="2022-12-01", end="2022-12-20" )

plt.subplot(3, 2, 1)
plt.plot(data1['Close'])
plt.title("2017", {'fontsize':15}) 
plt.subplot(3, 2, 2)
plt.plot(data2['Close'])
plt.title("2018", {'fontsize':15}) 
plt.subplot(3, 2, 3)
plt.plot(data3['Close'])
plt.title("2019", {'fontsize':15}) 
plt.subplot(3, 2, 4)
plt.plot(data4['Close'])
plt.title("2020", {'fontsize':15}) 
plt.subplot(3, 2, 5)
plt.plot(data5['Close'])
plt.title("2021", {'fontsize':15}) 
plt.subplot(3, 2, 6)
plt.plot(data6['Close'])
print(data6)
plt.title("2022", {'fontsize':15}) 
plt.show()