# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:25:31 2020

@author: imran
"""
import sys

liste = [4,'Apo',8,0]

for i in liste:
    try:
        print("sayı = "+ str(i))
        sonuc = 1/int(i)
        print("Sonuc = " + str(sonuc))
        
    except ValueError:
        print(str(i)+ " bir sayı değil")
        
    except ZeroDivisionError:
        print(str(i)+ " sıfır ile bölünemez")
        
    except:
        print("hesaplanamadı")  
        print("Sistem diyor ki : "+ str(sys.exc_info()[0]))
    finally:
        print("İşlemler bitti")
    
