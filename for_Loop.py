# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 00:10:41 2020

@author: imran
"""
numbers= [0,1,2,3,4,5,6,7,8,9,10]
toplam=0
sehirler= ["İstanbul","Ankara","İzmir"]

for sehir in sehirler:
    if sehir == "Ankara":
        print(sehir + " şehri için kod = " + sehir[0:3])
    print(sehir)
    
for number in numbers:    
    toplam= toplam + number
print(toplam)    

#BREAK VE CONTİNUE

for sehir in sehirler:
    if sehir == "Ankara":
        break
    print(sehir + " şehri için kod = " + sehir[0:3])
    print(sehir)
    
print("*****************")

for sehir in sehirler:
    if sehir == "Ankara":
        continue
    print(sehir + " şehri için kod = " + sehir[0:3])
    print(sehir)    

# RANGE FONKSİYONU

for x in range(0,100,2):
    print(x)
