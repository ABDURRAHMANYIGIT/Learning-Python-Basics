# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

ogrenciler = ["ali","ayşe"]

sehirler = list(("Ankara", "İstanbul", "Ankara"))

print("Ankara sayısı=" + str(sehirler.count("Ankara")))

print("Ankara indexi=" + str(sehirler.index("Ankara"))) #index = kaçıncı sırada olduğunu gösterir, ilk bulduğu yerde biter

sehirler.pop(1) #silmek
sehirler.insert(0,"İstanbul") #eklemek
sehirler.reverse() #terse çevirmek

print (sehirler)

sehirler2=sehirler

sehirler2[0]="İzmir"
print(sehirler)

sehirler.extend(sehirler2) #uzatmak, birleştirmek
print(sehirler)

sehirler.sort() #sıralamak 
print(sehirler)
print(type(ogrenciler))
print(type(sehirler))
