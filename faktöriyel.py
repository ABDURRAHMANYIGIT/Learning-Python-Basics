# -*- coding: utf-8 -*-

sayi = int(input("sayı nedir ?"))

faktoriyel = 1

if sayi<0:
    print("düzgün sayı ver lan it")
elif sayi == 0:
    print("cevabı 1 dir")
else:
    for x in range (1,sayi+1):
        faktoriyel = faktoriyel * x
    print(faktoriyel)
    
    