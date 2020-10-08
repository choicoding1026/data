
import pandas as pd
import numpy as np

user_usage = pd.read_csv("./data/user_usage.csv")
user_device = pd.read_csv("./data/user_device.csv")
devices = pd.read_csv("./data/android_devices.csv")


print("user_usage 데이터프레임: \n", user_usage)
print("user_device 데이터프레임: \n",user_device)
print("devices 데이터프레임: \n",devices)

### 코드 구현 ######
print("user_usage 데이터프레임: \n", user_usage)
print("user_device 데이터프레임: \n",user_device)
print("devices 데이터프레임: \n",devices)
devices.rename(columns={"Retail Branding": "manufacturer"}, inplace=True)

# First, add the platform and device to the user usage.
result = pd.merge(user_usage,
                 user_device[['use_id', 'platform', 'device']],
                 on='use_id',
                 how='left')

# Now, based on the "device" column in result, match the "Model" column in devices.
devices.rename(columns={"Retail Branding": "manufacturer"}, inplace=True)
result = pd.merge(result,
                  devices[['manufacturer', 'Model']],
                  left_on='device',
                  right_on='Model',
                  how='left')

xxx = result.groupby("manufacturer").agg({
        "outgoing_mins_per_month": "mean",
        "outgoing_sms_per_month": "mean",
        "monthly_mb": "mean",
        "use_id": "count"
    })
print(xxx)

### 코드 구현 ######