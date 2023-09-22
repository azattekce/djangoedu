
from functools import reduce

print("""
1'den N'e Kadar Sayı İşlemleri
""")

n=input("N değerine girebilir miisniz ? :")
list=range(1,int(n)+1)

print("1'den N kadar Çift Sayılar:",*filter(lambda x:x%2==0,list))

print("1'den N kadar Tek Sayılar:",*filter(lambda x:x%2==1,list))

print("1'den N kadar Tüm Sayıların Toplamı:",reduce(lambda x,y:x+y,list))

print("1'den N kadar Tüm Sayıların Çarpımı",reduce(lambda x,y:x*y,list))