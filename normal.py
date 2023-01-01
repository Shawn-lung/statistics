from scipy.stats import binom
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pandas as pd
# setting the values
# of n and p
n = 50
p = 0.58
# defining the list of r values
r_values = list(range(n + 1))
# obtaining the mean and variance 
Mean, var = binom.stats(n, p)
Std = var**1/2
# list of pmf values


print(Mean)
print(Mean - 2*Std)
print(Mean + Std*2)
x = np.linspace(Mean - 3*Std, Mean + 3*Std, 100)  # 創造 (平均數正負3個標準差之間的等差數列)
y = stats.norm.pdf(x, Mean, Std) # 將上面的等差數列找PDF，即 把x代入常態的PDF函數得到機率密度

plt.plot(x, y, 'k', label='normal pdf')
plt.axvline(Mean, color='b', linestyle='dashed', linewidth=2, label='Mean = 29')
plt.axvline(Mean-Std, color='g', linestyle='dashed', linewidth=2, label='Std = 6.1')
plt.axvline(Mean+Std, color='g', linestyle='dashed', linewidth=2)
plt.legend()  # 設置圖例的位置，()空的會預設最佳位置，可以自訂: loc='upper left', 'upper right', 'lower left', 'lower right',.....
#plt.legend(loc='upper left')  # 示例
plt.show()
# printing the table
