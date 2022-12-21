# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:34:49 2020

@author: imran
"""

AhmetHesap = {      
        'ad' : 'Ahmet Bey',
        'hesapNo': '5154652',
        'bakiye': 3000,
        'ekHesap' : 2000,
        }

MehmetHesap = {      
        'ad' : 'Mehmet Bey',
        'hesapNo': '5584652',
        'bakiye': 2000,
        'ekHesap' : 1000,
        }


def paraCek (hesap , miktar):
    print(f"Merhaba {hesap['ad']}")
    
    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print("paranızı alabilirsiniz")
        
    else:
        
        toplamPara = hesap['bakiye'] + hesap['ekHesap']
        
        ekHesapKullanılsınMı = input("Ek Hesabınız kullanılsın mı? (e/h)")
        
        if ekHesapKullanılsınMı == 'e':
            
            ekHesapKullanılacakMiktar = miktar - hesap['bakiye']
            hesap['bakiye'] = 0
            hesap['ekHesap'] -= ekHesapKullanılacakMiktar
            
            
            print("Paranızı alabilirsiniz")
            print(f"{hesap['hesapNo']} no'lu hesabınızda {hesap['ekHesap']} ek bakiye kalmıştır. ")
        else:
            print(f"{hesap['hesapNo']} no'lu hesabınızda {hesap['bakiye']} bakiye bulunmaktadır. ")
     

paraCek(AhmetHesap,5001)








