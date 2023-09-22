def double(x):
    return x*2

list1=[1,2,3,4,5,6,7,8,9]
newList=map(double,list1)

print("Map İşlemi:",*newList)

##example-1 :
print("Demet elemanların karesi:",*map(lambda x:x**2,(1,2,3,4,5,6,7,8,9)))
print("Listedeki elemanların küpü:",*map(lambda x:x**3,[1,2,3,4,5,6,7,8,9]))
print("İki Liste çarpımı:",*map(lambda x,y:x*y,[1,2,3,4,5],[6,7,8,9,10]))