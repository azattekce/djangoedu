import time
import time

print("******DECORETSİZ**********")
def kareleri_hesapla(sayılar):
    baslama = time.time()
    sonuç = []
    for i in sayılar:
        sonuç.append(i ** 2)
    bitis =  time.time()
    print(" kareleri_hesapla:" + str(bitis-baslama) + " saniye sürdü.")
    return sonuç

def küpleri_hesapla(sayılar):
    baslama = time.time()
    sonuç = []
    for i in sayılar:
        sonuç.append(i ** 3)
    bitis =  time.time()
    print(" küpleri_hesapla:" + str(bitis-baslama) + " saniye sürdü.")
    return sonuç
    

kareleri_hesapla(range(10000))

küpleri_hesapla(range(10000))

print("******DECORETE**********")