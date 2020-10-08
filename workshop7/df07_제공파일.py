

import numpy as np
import pandas as pd
from datetime import datetime

### 코드 구현 ######
# np.random.seed(123456)s
rng = pd.date_range( datetime.today().strftime('%Y-%m-%d'), periods=5, freq='D')  # Month
df = pd.DataFrame({'foo':np.random.randn(5), 'bar':range(10, 15)},
                  index=rng)
print(df.head())



### 코드 구현 ######



