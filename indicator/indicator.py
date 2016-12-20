def bbands(price, length=20, numsd=2):
    import numpy as np
    """ returns average, upper band, and lower band"""
    # print(price[['High', 'Low', 'Close']].sum(axis=1))
    mean = price[['High', 'Low', 'Close']].mean(axis=1)
    ave = mean.rolling(length).mean()
    sd = mean.rolling(length).std(ddof=0)
    upband = ave + (sd * numsd)
    dnband = ave - (sd * numsd)
    return np.round(upband, 0), np.round(ave, 0), np.round(dnband, 0)
