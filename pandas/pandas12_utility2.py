'''


'''
import pandas as pd
import numpy as np

# 1. 날짜를 index로 가져오기
data = pd.date_range(start="2020/01/01", end="2020/01/10")
print(data)

date_idx = pd.date_range("2020/01/01", periods=100)
df = pd.DataFrame({"price":range(100)}, index=date_idx)
print(df)

# 2. str -> date
print(pd.to_datetime('2020-01-01'))
print(pd.to_datetime('2020년01월01일 12시42분39초', format='%Y년%m월%d일 %H시%M분%S초'))

# 3. scientist 데이터에서 살아온 날짜 계산
df = pd.read_csv("./data/scientists.csv")
print(df)
days = pd.to_datetime(df['Died']) - pd.to_datetime(df['Born'])
print(days)
df['age_days'] = days
df['Born_year'] = pd.to_datetime(df['Born']).dt.year
df['Born_month'] = pd.to_datetime(df['Born']).dt.month
df['Born_day'] = pd.to_datetime(df['Born']).dt.day
print(df)

# 4. Datetime -> str
print(pd.to_datetime(df['Born']).astype(str))

