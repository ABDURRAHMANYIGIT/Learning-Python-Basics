# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 02:18:02 2020

@author: imran
"""

    
print("Operasyonlar :")
print("1 : topla")
print("2 : çıkar")
print("3 : çarp")
print("4 : böl")
sayi = int(input("Hangi işlemi yapmak istersiniz?"))
sayi1 = int(input("İlk sayı nedir?"))
sayi2 = int(input("İkinci sayı nedir?"))

class Matematik:
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        
    def topla(self):
        return self.sayi1+self.sayi2
        
    def cikar(self):
        return self.sayi1-self.sayi2
        
    def carp(self):
        return self.sayi1*self.sayi2
        
    def bol(self):
        return self.sayi1/self.sayi2
    
matematik = Matematik(sayi1, sayi2)

if sayi == 1:
    print(matematik.topla())

elif sayi == 2:
    print(matematik.cikar())
    
elif sayi == 3:
    print(matematik.carp())

else:
    print(matematik.bol())









    
    