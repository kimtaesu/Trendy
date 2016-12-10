import trendy
import csv
import pandas as pd

x = pd.read_csv('data\\014710_사조씨푸드.csv', names=['Date', 'Open', 'High', 'Low', 'Volume', 'Close'])
x = x.reindex(index=x.index[::-1])
trendy.gentrends(x['Close'])
