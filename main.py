import pandas as pd
import indicator.indicator as ta

x = pd.read_csv('data\\014710_사조씨푸드.csv', names=['Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'])
x = x.reindex(index=x.index[::-1])
upper, center, lower = ta.bbands(x)
