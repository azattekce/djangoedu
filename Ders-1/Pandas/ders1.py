import numpy as np
import pandas as pd
from  numpy.random import randn


df=pd.DataFrame(data=randn(3,3),index=["A","B","C"],columns=["Column-1","Column-2","Column-3"])

#print(df)

print("********************Kulalnıcı Tbalosu***********")

myfamily={"azat":35,"özge":30,"lina":0}
print(pd.Series(myfamily))

mydata=pd.Series(myfamily)

#dfMyFamily=pd.DataFrame(data=mydata,index=["A","B","C"],columns=["AD","YAS"])
#print(dfMyFamily)



df = pd.DataFrame({
    "Names":["Azat","Özge","Lina"],
    "Yas":[35,32,0],
    "Doğrum Yeri":["Iğdır","Adıyaman","Tekirdağ"]
})

print(df[df["Yas"]>30])


print("Yaş:",df[df["Names"]=="Azat"]["Yas"])


dataset = pd.read_excel("tuketim.xlsx")

print(dataset["FARK_SAAT"].str.contains("137"))
