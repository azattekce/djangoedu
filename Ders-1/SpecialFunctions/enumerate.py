liste=["ANNE","BABA","AZAT","ÖZGE"]


i=0
list2=list()

while(i<len(liste)):
    list2.append((i,liste[i]))
    i+=1
print(*list2)

"""ENUMERATE FONKİSYONU İLE ÇOK BASİT"""

print("ENUMERATE İLE:",*enumerate(liste))

for i,j in enumerate(liste):
    print("İndex:{},Value:{}".format(i,j))