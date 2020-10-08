'''


'''
import pandas as pd
import numpy as np

df = pd.read_csv("./data/gapminder.tsv", sep="\t")
print(df.head())

# 1. replace
df2 = df['continent'].str.replace('Asia', 'EU')
print(df2.head())

# 2. slice
df2 = df['country'].str[:5]
print(df2.head())

# 3. startswith
df2 = df['country'].str.startswith('A')
print(df[df2])

# 4. endswith
df2 = df['country'].str.endswith('a')
print(df[df2])

# 5. contains
df2 = df['country'].str.contains('ur')
print(df[df2])

# 6. lower, upper, swapcase 등 str 함수 적용 가능