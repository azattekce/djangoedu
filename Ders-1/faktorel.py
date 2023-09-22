print("""
      
FAKTÖREL ALMA
      
      """)




while True:
  sayi=input("Faktöreli hesaplanacak sayi giirn :")
  if(sayi=="q"):
     print("Program solandı.")
     break
  else:
     sayi=int(sayi)
     faktorle=1
     for i in range(2,sayi+1):
        faktorle=faktorle*i
    
     print("Faktorel:",faktorle)