# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:33:01 2020

@author: imran
"""

class Matematik:
    def topla(self,sayi1,sayi2):
        return(sayi1+sayi2)
        
    def cikar(self,sayi1,sayi2):
        return(sayi1-sayi2)
        
    def carp(self,sayi1,sayi2):
        return(sayi1*sayi2)
        
    def bol(self,sayi1,sayi2):
        return(sayi1/sayi2)

matematik= Matematik()
print("Toplam = " + str(matematik.topla(2,32)))

#%%
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

matematik= Matematik(2,65)
print("Toplam = " + str(matematik.topla()))
#%% Property

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
person1 = Person("apo","yiğit",16)
print(person1.lastName)
#%% Inheritance

class Worker(Person):
    def __init__(self,salary,lastName):
        self.salary = salary
        self.lastName = lastName
        
class Customer(Person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber

ahmet = Worker("1500","Çakır")

mehmet = Customer("051645124864")

print(ahmet.salary)
print(ahmet.lastName)
print(mehmet.creditCardNumber)
