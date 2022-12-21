# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 23:29:29 2020

@author: imran
"""
import json

with open("users.json") as users:
    data = json.load(users)
    
    print(data[0]["username"])
    print(data[0]["email"])
    print(data[0]["phone"])
    print(data[0]["address"]["street"])
