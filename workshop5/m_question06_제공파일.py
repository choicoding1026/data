
import pandas as pd
import numpy as np

user_usage = pd.read_csv("./data/user_usage.csv")
user_device = pd.read_csv("./data/user_device.csv")
devices = pd.read_csv("./data/android_devices.csv")


### 코드 구현 ######
print("1. devices에서 Model명이 'SM-G930F' 검색:")
print(devices[devices.Model == 'SM-G930F'])
print()
print("2. devices에서 Device명이 'GT' 로 시작하는 데이터 검색:")
print(devices[devices.Device.str.startswith('GT')])

### 코드 구현 ######

