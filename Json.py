# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 23:18:21 2020

@author: imran
"""

import json

data = '{"firstName":"Abdurrahman","lastName":"Yiğit"}'

y = json.loads(data)

print(y["firstName"])
print(y["lastName"])


customer = {
        "firstName":"Ali",
        "lastName":"Demir"
        }

customerJson=json.dumps(customer)
print(customer)