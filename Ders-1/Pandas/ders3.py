import numpy as np
import pandas as pd
from  numpy.random import randn



outerIndex = ["Group1","Group1","Group1","Group2","Group2","Group2","Group3","Group3","Group3"]
innerIndex = ["Index1","Index2","Index3","Index1","Index2","Index3","Index1","Index2","Index3"]

lits = list(zip(outerIndex,innerIndex))

df = pd.MultiIndex.from_tuples(lits)

hierarchy = pd.DataFrame(randn(9,3),df,columns=["Column-1","Column-2","Column-3"])





print(hierarchy)