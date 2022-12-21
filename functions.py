# -*- coding: utf-8 -*-

def selamVer(isim ="dostum"):
    print("merhaba "+ isim)
    
selamVer("apo")
selamVer("ali")
selamVer("ahmet")
selamVer("eren")
selamVer()

def selamVer2(isim="ziyaretçi", soyİsim= " arkadaş"):
    print("merhaba "+ isim + soyİsim)

selamVer2()
selamVer2("apo"," yiğit")

#RETURN EDEN FONKSİYONLAR

#%%
def dikUcgenAlani(a,b):
    return a*b/2

alan = dikUcgenAlani(6,9)

print(alan)

#LAMBDA YUKARIDAKİ İLE AYNI AMA SADECE KISA YOLDAN YAZIMI İÇİN KULLANILIYOR
#%%

dikUcgenAlani2 = lambda a,b : a*b/2
print(dikUcgenAlani2(6,89))

x = dikUcgenAlani2
print(x(6,44)) #İKİ TÜRLÜ DE YAZILABİLİR




