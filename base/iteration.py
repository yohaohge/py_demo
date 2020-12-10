#-*-coding:utf-8-*- 


list = [1,2,3,4]
for i in list:
    print(i)
dict = {"Mike":18, "Lily":20, "Jack":21}

for key in dict:
    print(key, dict[key])

for ch in "ABCD":
    print(ch)

from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance(list, Iterable))
print(isinstance(dict, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
      print(i, value)

for i, value in  [(1, 1), (2, 4), (3, 9)]:
      print(i, value)
