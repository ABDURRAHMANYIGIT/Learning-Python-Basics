# -*- coding: utf-8 -*-

sayilar = [1,2,3,4,5,6,7,8,9,10]

ortalama = 0

for x in range (1,len(sayilar)+1):
    ortalama = ortalama + x 

ortalama = ortalama/ len(sayilar)

print(ortalama)