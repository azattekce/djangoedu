import numpy as np
import pandas as pd
from  numpy.random import randn


df = pd.read_excel("tuketim.xlsx")

#print(df.drop(["FARK_SAAT"],axis=1))

#df1=df.drop(["FARK_SAAT"],axis=1)

#df1.to_excel("tuketimchangced.xlsx")

newdata=pd.read_html("https://joker.opetcloud.net/Otobil/BMReport?reportTypeId=1")
print(newdata[0])