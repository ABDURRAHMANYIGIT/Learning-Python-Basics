# -*- coding: utf-8 -*-
birler=[" ","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar=[" ","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
yüzler=[" ","yüz"]
binler = [" ","bin"]
milyon = [" ","milyon"]
milyar = [" ","milyar"]

girilenSayi = input("1-11 Basamak Arası Bir Sayı Giriniz :")

basamakSayisi = len(girilenSayi)
girilenSayi = int(girilenSayi)

if basamakSayisi==11:
    onbir1 = girilenSayi %10000000000 #12345678954
    onbir2 = girilenSayi - onbir1 #10000000000
    onbir3 = onbir2//10000000000 #1
    onbir4 = onbir3 #1
    onbir5 = onlar[onbir4] #on yazdıracak milyar eklenecek aşşağıda
    on0 = girilenSayi - onbir2 #2345678954
    basamakSayisi = basamakSayisi-1
    
if basamakSayisi==10:
    on1 = on0 %1000000000 #2345678954
    on2 = on0 - on1 #2000000000
    on3 = on2//1000000000 #2
    on4 = on3 #2
    on5 = birler[on4] #iki yazdıracak milyar eklenecek aşşağıda
    dokuz0 = on0-on2 #345678954
    basamakSayisi = basamakSayisi-1
    
if basamakSayisi==9:
    dokuz1 = dokuz0 %100000000 #345678954
    dokuz2 = dokuz0 - dokuz1 #300000000
    dokuz3 = dokuz2//100000000 #3
    dokuz4 = dokuz3 #3
    dokuz5 = birler[dokuz4] #üç yazdıracak sonunda yüz ve milyon eklenecek aşşağıda
    sekiz0 = dokuz0-dokuz2 #45678954
    basamakSayisi = basamakSayisi-1
    
if basamakSayisi==8:
    sekiz1 = sekiz0 %10000000 #45678954
    sekiz2 = sekiz0 - sekiz1 #40000000
    sekiz3 = sekiz2//10000000 #4
    sekiz4 = sekiz3 #4
    sekiz5 = onlar[sekiz4] #kırk yazdıracak sonuna milyon eklenecek aşşağıda
    yedinci0 = sekiz0-sekiz2 #5678954
    basamakSayisi = basamakSayisi-1
    
if basamakSayisi==7:
    yedinci1 = yedinci0 %1000000 #5678954
    yedinci2 = yedinci0 - yedinci1 #5000000
    yedinci3 = yedinci2//1000000 #5
    yedinci4 = yedinci3 #5
    yedinci5 = birler[yedinci4] #beş yazdıracak milyon eklenecek
    altıncı0 = yedinci0 - yedinci2 #678954 
    basamakSayisi = basamakSayisi-1
       
if basamakSayisi == 6:
    altıncı1 = altıncı0%100000 #678954 
    altıncı2 = altıncı0 - altıncı1 #600000
    altıncı3 = altıncı2//100000 #6
    altıncı4 = altıncı3 #6
    altıncı5 = birler[altıncı4] #6 yazdıracak sonunda yüz ve bin eklenecek
    beşinci0 = altıncı0-altıncı2 #78954
    basamakSayisi = basamakSayisi-1
    
if basamakSayisi == 5:
    beşinci1 = beşinci0%10000 #78954
    beşinci2 = beşinci0 - beşinci1 #70000
    beşinci3 = beşinci2//10000 #7
    beşinci4 = beşinci3 #7
    beşinci5 = onlar[beşinci4] #yetmiş yazdıracak sonuna bin eklenecek aşşağıda
    dördüncü0 = beşinci0-beşinci2 #8954
    basamakSayisi = basamakSayisi-1
    
if basamakSayisi==4:
    dördüncü1 = dördüncü0 %1000 #8954
    dördüncü2 = dördüncü0 - dördüncü1 #8000
    dördüncü3 = dördüncü2//1000 #8
    dördüncü4 = dördüncü3 #8
    dördüncü5 = birler[dördüncü4] #sekiz yazdıracak sonuna bin eklenecek
    üçüncü0 = dördüncü0-dördüncü2 #954
    basamakSayisi = basamakSayisi-1
    
    
if basamakSayisi==3:
    üçüncü1 = üçüncü0 % 100 #954
    üçüncü2 = üçüncü0- üçüncü1 #900
    üçüncü3 = üçüncü2 // 100 #9 
    üçüncü4 = üçüncü3 #9
    üçüncü5 = birler[üçüncü4] #dokuz yazdıracak sonuna yüz eklenecek aşşağıda
    ikinci0 = üçüncü0-üçüncü2 #54
    basamakSayisi = basamakSayisi-1
    
if basamakSayisi==2: 
    ikinci1 =  girilenSayi%10 #54
    ikinci2 = ikinci0 - ikinci1
    ikinci3 = ikinci1 // 10 #5
    ikinci4 = ikinci3 #5
    ikinci5 = onlar[ikinci4] #elli yazdıracak
    birinci0 = ikinci0-ikinci2 #54-50=4
    basamakSayisi = basamakSayisi-1
    
if basamakSayisi==1:
    birinci = birler[birinci0] #dört yazdıracak
    
print(onbir5 +" "+ on5 +" "+ milyar[1] +" "+ dokuz5 +" "+ yüzler[1] +" "+ sekiz5 +" "+ yedinci5 +" "+ milyon[1] +" "+ altıncı5 +" "+ yüzler[1] + " " + beşinci5 +" "+  dördüncü5 + " " + binler[1] +" "+ üçüncü5 + " " + yüzler[1] +" "+ ikinci5 +" "+ birinci )