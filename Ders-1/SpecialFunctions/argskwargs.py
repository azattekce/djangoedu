

def functionArgs(*args):
     for i in args:
      print(i)


      
def functionKwargs(**kwargs):
     for i,j in kwargs.items():
      print("Key:{},Value:{}".format(i,j))


functionArgs(1,2,4,5)
functionKwargs(Name="AZAT",SurName="Tekçe",Age=36)