
a=input("Birinci sayi girin")
b=input("Birinci sayi girin")



try:
    print(int(a)/int(b))
    print("İşlem başarılı")
except  Exception as e:
    print("İşlem anında hata çıktı hata{}".format(e))

finally:
     print("Programın çalışması bitti.")

if(int(a)==100):
    raise  ValueError("Lütfen doğru bir input girin.")

