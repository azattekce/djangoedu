
sayac=3
while True:
    name=input("Lütfen adınız girin :")
    pswd=input("Lütfen şifre girin :")

    if(name=="azat" and pswd=="215454"):
       print("Başarılı giriş yapıldı.")
       break
    else:
     print("Kullanıcı bilgileri hatalı ...")
     sayac-=1
 
    if(sayac==0):
         print("Hatalı giriş sayısını aştınız.")
         break