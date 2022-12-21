# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:01:35 2020

@author: imran
"""

mySet= {"apo","apo"}
print(mySet)
mySet= {"a","p","o"}
print(mySet)

for mySet2 in mySet:
    print(mySet2)
    
if "p" in mySet:
    print("listede var")    
    
mySet.add("Ali")
print(mySet)

mySet.update(["2","4","3"])    
print(mySet)

print(len(mySet)) #uzunluğunu belirtir, kaç eleman olduğunu gösterir.

mySet.remove("Ali")#çıkartma işlemi yapar, 2 kere yaparsan hata verir çünkü set unique dir.
print(len(mySet))

mySet.discard("ali") #bu da çıkarır ama eğer setin içerisinde çıkarmak istediğin elemanı bulamazsa hata vermez.
print(len(mySet))



mySet.clear()
print(mySet)
