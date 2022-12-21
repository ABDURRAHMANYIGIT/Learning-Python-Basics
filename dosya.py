# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:09:40 2020

@author: imran
"""

#r okuma
#w yazma, dosya yoksa öyle bir dosya oluşturur
#a hem okyuacağım, hem de yazacağım. yani a da yeni dosya açıyor
#x oluştur


f = open("isimler.txt","r")

#print(f.read())
#
#print(f.readline())
#print(f.readline())
#print(f.readline())

for l in f:
    print(f.read())
    
f.close()

fileToAppend = open("öğrenciler.txt","a")
fileToAppend.write("apo")
fileToAppend.write("\n")
fileToAppend.write("yiğit")
fileToAppend.close()


#%%
import os

if os.path.exists("isimler.txt"):
    os.remove("isimler.txt")
else:
    print("öyle bir dosya yok")
#%%
os.rmdir("empty")




