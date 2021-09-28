import numpy as np 
import pandas as pd 
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# ^GSPC (S&P 500)
# ^IXIC (NASDAQ)
# ^GDAXI (German DAX)
# ^FTSE (London FTSE)

# ytickers = ['^GSPC', '^IXIC', '^GDAXI', '^FTSE'] #indices/stocks
ytickers = ['ETH-USD', 'BTC-USD', 'XTZ-USD', 'ADA-USD', 'TRX-USD'] #crypto

ind_data = pd.DataFrame()

for t in ytickers:
	ind_data[t] = wb.DataReader(t, data_source='yahoo', start='2021-9-18')['Adj Close']

# print (ind_data.head())


(ind_data / ind_data.iloc[0] * 100).plot(figsize=(15, 6));
plt.title("Crypto Rate of Return")
plt.xlabel("Time Horizon")
plt.ylabel("Normalized to 100")
plt.axhline(y=100, color='r', linestyle='--')
plt.show()

