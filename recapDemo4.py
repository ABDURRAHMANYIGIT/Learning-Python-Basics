# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:13:01 2020

@author: imran
"""

ogrenciler = ["ali","ayşe","ahmet","mehmet"]

fileToAppend = open("ogrenciler.txt","a")

for ogrenci in ogrenciler:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")
    
fileToAppend.close()