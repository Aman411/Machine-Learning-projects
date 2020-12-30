import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.figure(figsize=(15,5))
s = pd.Series(np.arange(10)**2)
plt.subplot(2,2,1)
s.plot(kind='line')
plt.xticks(s.index)
plt.subplot(2,2,2)
s.plot(kind='bar')
plt.xticks(s.index)
plt.subplot(2,2,4)
s.plot(kind='bar')
plt.xticks(s.index)
plt.show()