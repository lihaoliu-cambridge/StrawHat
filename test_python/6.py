from pandas import DataFrame as df
import numpy as np

d1 = df(np.random.randn(7, 3))
d1.ix[:4, 3] = None
d1.ix[:2, 2] = None
print d1
print d1.dropna(thresh=3)
