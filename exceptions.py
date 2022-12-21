# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:20:12 2020

@author: imran
"""

try:
    sayi = int(input("Sayı giriniz"))

except ZeroDivisionError:
    print("Payda 0 olamaz")
    
except ValueError:
    print("Tip uyuşmazlığı: Lütfen SAYI giriniz")   
    
except:
    print("Hata oluştu.")
