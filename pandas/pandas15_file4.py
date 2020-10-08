'''
    HTML file
    * pip install lxml
    1. read
        pd.read_html(filename, option)
        pd.read_html(url, option)
    2. write
        df.to_html(filename, option)
'''

import pandas as pd
import numpy as np

df = pd.read_html("http://www.seoul.go.kr/coronaV/coronaStatus.do")

print("갯수: ", len(df))
print("코로나 현황 DataFrame \n", df[3].head())

new_df = df[3][:100]
new_df.to_csv("./data/coronaV1.csv")


