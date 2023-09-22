
class Book():
    def __init__(self,name,page):
        self.name=name
        self.page=page
    def __str__(self):
        return """ 
               KİTAP ÖZELİKLER 
               Kitab adı:{}\n
               Kitap SayfaSI:{} 
               """.format(self.name,self.page)
    def __len__(self):
         return self.page
    
    def __del__(self):
         print("Kitiap silindi.")

myBook=Book("HAYAT GÜZELDİR",200)
del myBook
print(myBook)