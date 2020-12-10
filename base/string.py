#-*-coding:utf-8-*- 

print('string')
print('中文字符串')
print("双引号字符串")
print("双引号字符串")

#字符串编码
s='Python中文'
print(s)
#b = s.encode('utf-8') # some problems in here
#print(b)
#print(b.decode('utf-8'))

#格式化
print('Age: %s. Gender: %s' % (25, True))
print( 'growth rate: %d %%' % 7)
print( 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

