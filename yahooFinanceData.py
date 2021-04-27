#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 12:58:07 2021

@author: yoko
"""

import yfinance

# import matplotlib as plt
# import seaborn

aapl = yfinance.Ticker("AAPL")
print(aapl)
"""
returns
<yfinance.Ticker object at 0x1a1715e898>
"""

# get stock info
aapl.info

"""
returns:
{
 'quoteType': 'EQUITY',
 'quoteSourceName': 'Nasdaq Real Time Price',
 'currency': 'USD',
 'shortName': 'Microsoft Corporation',
 'exchangeTimezoneName': 'America/New_York',
  ...
 'symbol': 'MSFT'
}
"""

# get historical market data, here max is 5 years.
# hist = aapl.history(period="max")
hist = aapl.history(period="1y")
print(hist)

hist['Close'].plot(figsize=(16, 9))
