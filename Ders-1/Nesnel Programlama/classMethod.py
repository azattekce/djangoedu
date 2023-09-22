
from typing import Any
import datetime 


class Araba():
    def __init__(self,model,year):
       self.model=model
       self.year=year
    def ArabaYasihesapla(self):
        return int(datetime.datetime.now().year)-int(self.year)



myCar=Araba("Renault Cilo",2014)
print(" Araba Modeli:{}".format(myCar.model)," Araba yaşı:{}".format(myCar.ArabaYasihesapla()))