# -*- coding: utf-8 -*-

set1 = {1,2,3,4,5,6,7}
set2 = {1,2,8,6,9,16}

print(set1 | set2)
print(set1.union(set2))  # BİRLEŞİM

print(set1 & set2)
print(set1.intersection(set2))  # KESİŞİM

print(set2 - set1)
print(set1 - set2)
print(set1.difference(set2)) # A - B
print(set2.difference(set1)) # B - A

print(set1 ^ set2)
print(set1.symmetric_difference(set2)) # (A - B) + (B - A)