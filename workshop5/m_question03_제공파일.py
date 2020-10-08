
import pandas as pd
import numpy as np

user_usage = pd.read_csv("./data/user_usage.csv")
user_device = pd.read_csv("./data/user_device.csv")
devices = pd.read_csv("./data/android_devices.csv")


### 코드 구현 ######
devices.rename(columns={'Retail Branding':'manufacturer'}, inplace=True)
result = pd.merge(user_usage, user_device[['use_id', 'platform', 'device']], how="right", on="use_id")
print(result.head())
### 코드 구현 ######
