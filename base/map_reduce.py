# -*- coding: utf-8 -*-
def f(x):
    return x * x

r = map(f, range(1,10))
print(r)

r = map(str, range(1,10))
print(r)

def add(x,y):
    return x + y

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
r = reduce(add, range(1,100))
print(r)

def fn(x,y):
    return x * 10 + y;
r = reduce(add, range(1,100))
