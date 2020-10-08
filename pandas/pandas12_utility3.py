'''


'''
import pandas as pd
import numpy as np

omh = pd.read_csv("./data/omh.csv")
print(omh.head())

print("특정 컬럼 최소값: ", omh['MSFT'].min())
print("복수 컬럼 최소값 \n", omh[['MSFT','AAPL']].min())
print("특정 컬럼 최소값의 index \n", omh[['MSFT','AAPL']].idxmin())

print("특정 컬럼 최대값: ", omh['MSFT'].max())
print("복수 컬럼 최대값 \n", omh[['MSFT','AAPL']].max())
print("특정 컬럼 최대값의 index \n", omh[['MSFT','AAPL']].idxmax())

print("특정 컬럼 최대값 n개\n", omh.nlargest(3, ['MSFT']))
print("특정 컬럼 최대값 n개\n", omh['MSFT'].nlargest(3))

print("특정 컬럼 최소값 n개 \n", omh.nsmallest(3, ['MSFT']))
print("복수 컬럼 최소값 n개 \n", omh['MSFT'].nsmallest(3))

# sum 합, cumsum 누적합, prod 곱, cumprod 누적곱, mean 평균,