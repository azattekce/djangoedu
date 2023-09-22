from datetime import datetime

def KareAll():
    list=[]
    for i in range(1,10):
        list.append(i**2)
    return list

##print(KareAll())

print("********GENERATOR İLE *******")

def KareAllG():
     for i in range(1,10):
        yield i**2

##print(*KareAllG())

print(datetime.strftime(datetime.now(),"%B-%A-%Y"))