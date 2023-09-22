from functools import reduce


print("""
1'den N'e Toplam Hesaplama
""")

n=input("N değerine girebilir miisniz ? :")

list=range(1,int(n)+1)

print("Toplnacak sayılar:",*list)


def toplama(x,y):
    return x+y

print("1'den N kadar toplam:",reduce(toplama,list))

print("N!:",reduce(lambda x,y:x*y,list))


def max(x,y):
    if(x>y):
      return x
    else:
       return y

print("Max :",reduce(max,(2,5,8,9,4)))


