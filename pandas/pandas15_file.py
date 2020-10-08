'''
    csv file(구분자: comma)
    1. read
        pd.read_csv(filename, option)
    2. write
        df.to_csv(filename, option)
'''

import pandas as pd
import numpy as np

# 1. read
df = pd.read_csv("./data/msft.csv")
print(df.head())

df = pd.read_csv("./data/msft.csv", index_col=0)
print(df.head())

df = pd.read_csv("./data/msft.csv", header=0, names=['date', 'open', 'high', 'low', ' close', 'volume'])
print(df.head())

df = pd.read_csv("./data/msft.csv", usecols=['Volume','High','Low','Date'], index_col=0)
print(df.head())

df = pd.read_csv("./data/msft.csv", skiprows=[1,2,3,4,5], header=0)
print(df.head())

df = pd.read_csv("./data/msft.csv", nrows=8)
print(df)

df = pd.read_csv("./data/msft.csv", skiprows=100, nrows=10)
print(df)

# .tsv, .txt ..
df = pd.read_csv("./data/msft_piped.txt", sep="|", index_col=0)
print(df.head())

df = pd.read_csv("./data/gapminder.tsv", sep="\t", index_col=0)
print(df.head())
new_df = df[:10]
print(new_df)
new_df.to_csv("./data/new_df.csv")

