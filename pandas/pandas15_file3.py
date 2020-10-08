'''
    JSON file
    1. read
        pd.read_json(filename, option)
    2. write
        df.to_json(filename, option)
'''

import pandas as pd
import numpy as np

df = pd.read_json("./data/stocks.json")
print(df)

new_df = df[:4]
print(new_df)
new_df.to_json("./data/new_df.json")


