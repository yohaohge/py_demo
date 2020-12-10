# -*- coding: utf-8 -*-
def power(x, n=2): # 默认值
    s = 1
    while n > 0: 
        n = n - 1
        s = s * x
    return s

print(power(5))

def calc(*numbers): # 可变参数
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2))
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))
print(calc(*nums)) # *nums表示把nums这个list的所有元素作为可变参数传进去

def person(name, age, **kw): # 关键字参数
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
person('Jack', 24, city='Beijing', job='Engineer')
person('Jack', 24, job='Engineer')
person('Jack', 24)