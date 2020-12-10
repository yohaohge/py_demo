#-*-coding:utf-8-*- 

# 列表生成器
list = range(1,11)
print(list)

list = [x * x for x in range(1, 11)]
print(list)

list = [m + n for m in 'ABC' for n in 'XYZX']
print(list)

list = [x for x in range(1, 11) if x % 2 == 0] # 筛选
print(list)

list = [x if x % 2 == 0 else 0 for x in range(1, 11) ]
print(list)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k,v)