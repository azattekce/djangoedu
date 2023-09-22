
class Araba():
 def __init__(self,model,year,fuelType,color):
    self.model=model
    self.year=year
    self.fuelType=fuelType
    self.color=color
    print("Araba sınıf çağrıldı.")


class Araba1():
    model="Renult"
    year=2014
    fuelType="Benzin"
    color="Beyaz"
    def __init__(self):
     print("Araba1 sınıf çağrıldı.")


myCar=Araba("Cilo",2014,"Benzin","Beyaz")


tahirAbi=Araba1()
tahirAbi.color="Grey"
tahirAbi.fuelType="Dizel"
tahirAbi.model=2012
tahirAbi.model="Symbol"

print( "Tahir :{}".format(tahirAbi.model),"Azat:{}".format(myCar.model))

print(dir(Araba1),"\n *******\n",dir(Araba))

