import numpy as np
import pandas as pd
from  numpy.random import randn


data={
    "Ürün":["Motorin","Dizel","LPG"],
    "2018":[3,4,5],
    "2019":[20,10,10],
    "2020":[40,40,40]
}



df=pd.DataFrame(data)
print("** tüm Liste **** \n")


df.set_index("Ürün",inplace=True)

print(df)

df["Toplam"]=df["2018"]+df["2019"]+df["2020"]

print("**Topam eklenmiş Liste **** \n")
print(df)


print("** LPG Toplam **** \n")

print(df.loc["LPG"]["Toplam"])

print("** Tüm Toplam **** \n")

print(df.loc["Motorin"]["Toplam"]+df.loc["LPG"]["Toplam"]+df.loc["Dizel"]["Toplam"])



print("**Toplamı 54'den fazlan olanlar **** \n")

print(df[df["Toplam"]>54])