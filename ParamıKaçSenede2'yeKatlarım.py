# -*- coding: utf-8 -*-

import math

getiri = int(input("Yaptığınız işin yıllık getiri yüzdesi kaçtır ?"))

getiri = getiri/100

kaçYil = math.log10(2)/math.log10(1+getiri)

print(kaçYil)