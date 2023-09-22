from typing import Any

class Person():
    def __init__(self, name,surName,age,mail,salary):
        self.name=name
        self.surName=surName
        self.age=age
        self.mail=mail,
        self.salary=salary
    def GetInfo(self):
        print("""
        Kişisel Bilgileri:\n
        Ad:{}\n
        Soyad:{}\n
        Yaş:{}\n
        Mail:{}\n 
        Maaş:{}           
        """.format(self.name,self.surName,self.age,self.mail,self.salary))   

       

class Teacher(Person): ##overrading yapılmamış
      def SetSalary(self,salary):
        self.salary+=salary 


class Manager(Person): ##overrading yapılmamış ve süper anahtar eklenmiş
    def __init__(self, name,surName,age,mail,yetki):
        super().__init__(self, name,surName,age,mail)
        self.yetki=yetki
    def GetInfo(self):
                print("""
                Öğrenci Bilgileri:\n
                Ad:{}\n
                Soyad:{}\n
                Yaş:{}\n
                Mail:{}\n 
                Yetki:{}           
                """.format(self.name,self.surName,self.age,self.mail,self.yetki))  


class Student(Person): ##overrading yapılmış
      def __init__(self, name,surName,age,mail,sesion):
        self.name=name
        self.surName=surName
        self.age=age
        self.mail=mail,
        self.sesion=sesion
      def GetInfo(self):
            print("""
            Öğrenci Bilgileri:\n
            Ad:{}\n
            Soyad:{}\n
            Yaş:{}\n
            Mail:{}\n 
            Bölümü:{}           
            """.format(self.name,self.surName,self.age,self.mail,self.sesion))  






ogretmen=Teacher("Özge","TEKÇE",30,"ozgetekce@gmail.com",20000)
                 
student=Student("Demir","TEKÇE",30,"demirtekce@gmail.com","Sayısal")

manager=Manager("Azat","TEKÇE",36,"demirtekce@gmail.com","Müdür")


ogretmen.GetInfo()
ogretmen.SetSalary(5000)
print("************ ZAM SONRASI********")
ogretmen.GetInfo()
print("************ Öğrenci********")
manager.GetInfo()
student.GetInfo()
print("************ MÜDÜR********")
manager.GetInfo()
