#-*-coding:utf-8-*- 


L = [x * x for x in range(10)]
print(L)

# 生成器
g = (x * x for x in range(10)) #generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值
print(g)
print(next(g))
print(next(g))

for n in g:
    print(n)

# 这里，最难理解的就是generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行
# 遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

f = fib(6)

for n in f:
    print(n)

def triangles():
    list = [1]
    while True:
        tmp = list[0:]
        yield tmp
        for i in range(1,len(list)):
            list[i] = tmp[i] + tmp[i-1]
        list.append(1)

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)


