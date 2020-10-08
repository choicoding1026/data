

import pandas as pd
import numpy as np

df = pd.read_csv('data/sample_data.csv', index_col=0)
print(df)
### 코드 구현 ######
print(df.loc[df['height']>170, ['state','height','score']]) # boolean 색인

### 코드 구현 ######