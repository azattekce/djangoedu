list1=[1,2,3,4,5]
list2=[6,7,8,9,10,12]

i=0
list3=list()
while(i<len(list1) and i<len(list2)):
    list3.append((list1[i],list2[i]))
    i+=1
print(*list3)

"""ZİP FONKİSYONU İLE ÇOK BASİT"""


print("ZİP İLE:",*zip(list1,list2))