import os 


for klasör_yolu,klasör_isimleri,dosya_isimler  in os.walk("C:/Users/00004740/Desktop"):
    for i in dosya_isimler:
        if (i.endswith (".txt")):
            print("Dosya Adı:{}".format(i))
            print("*******************************************************************")
