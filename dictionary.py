# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 23:45:03 2020

@author: imran
"""

sozluk = {
         "table":"masa",
         "pencil":"kalem"
         }

sozluk2 = dict(kitap="book", anan="mother")

del (sozluk["table"])
print(sozluk)
print(sozluk2)

# set de {} kullanıyor iken ikisinin karışmama sebebi içine yazdıklarımızdır. yani dictionary olmasının sebebi içine dictionary
# ye göre bişey yazdığından dolayı eğer set'lik bişey yazsaydın set olurdu.