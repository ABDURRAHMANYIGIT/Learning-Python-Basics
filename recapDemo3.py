# -*- coding: utf-8 -*-

sayi = int(input("sayı nedir ?"))
asalMi = True

for x in range(2,sayi):
    if(sayi % x) == 0:
        asalMi = False
        break
    
if asalMi:
    print("asal")
else:
    print("asal değil")
        


    
    