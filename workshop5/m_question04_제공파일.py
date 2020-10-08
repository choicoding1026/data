
import pandas as pd
import numpy as np

user_usage = pd.read_csv("./data/user_usage.csv")
user_device = pd.read_csv("./data/user_device.csv")
devices = pd.read_csv("./data/android_devices.csv")

### 코드 구현 ######
devices.rename(columns={'Retail Branding':'manufacturer'}, inplace=True)
result = pd.merge(user_usage, user_device[['use_id', 'platform', 'device']], how="outer", on="use_id", indicator=True)
print(format(result.shape))

def kkkk(n):
    print(">>1", n)
    print(">>2", n.isnull())
    return n.isnull().sum()

print(format((result.apply(lambda x: x.isnull().sum(), axis=1) == 0).sum()))

### 코드 구현 ######

