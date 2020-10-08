'''
    excel file
    * pip install xlrd
    * pip install xlwt
    1. read
        pd.read_excel(filename, option)
    2. write
        df.to_excel(filename, option)
'''

import pandas as pd
import numpy as np

df = pd.read_excel("./data/stocks.xlsx") # sheet 2개(msft, aapl)
print(df.head())

df = pd.read_excel("./data/stocks.xlsx", sheet_name='aapl')
print(df.head())

df = pd.read_excel("./data/stocks.xlsx", sheet_name='aapl', skiprows=100, nrows=10, header=0, names=['D','O','H','L','C','V'])
print(df)
# df.to_excel("./data/new_df.xls")
df.to_excel("./data/new_df2.xls", sheet_name="new_df")

