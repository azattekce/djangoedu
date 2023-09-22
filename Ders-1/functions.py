def Faktorel(say):
    if(say==1):
      return 1
    return say*Faktorel(say-1)

def Write(say):
    if(say==1):
      return 1
    return  str(say)+","+str(Write(say-1))



print(Faktorel(5))
print(Write(50))