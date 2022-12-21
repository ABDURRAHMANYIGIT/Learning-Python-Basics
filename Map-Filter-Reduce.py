# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:42:11 2020

@author: imran
"""
from functools import reduce
sayilar = [1,2,3,4,5]

#sayilarKaresi = []
#for sayi in sayilar:
#    sayilarKaresi.append(sayi*sayi)

sayilarKareli = list(map(lambda sayi: sayi*sayi, sayilar))

print(sayilarKareli)


sayilarFiltreli = list(filter(lambda sayi: sayi>2,sayilar))
print(sayilarFiltreli)


sayilarFakrotiyel = reduce(lambda x,y:x*y,sayilar)
print(sayilarFakrotiyel)
