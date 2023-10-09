
import numpy as np

datalist=[10,20,30]

arr = np.array(datalist)

#print(*range(0,100,3))
#print(*np.arange(0,100,3))

ar1=np.arange(1,21)
ar2=ar1.reshape(4,5)
print(ar2)

print("****tüm satırların 2 stünları ****** \n")
print(ar2[:,:2])

print("******Tüm satırların  sadece 3ten sonrakiler******\n")
print(ar2[:,2:])


print("******ilk iki stünr******\n")
print(ar2[:2,:])