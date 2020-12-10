#dict 
dic={"Mike":19,"Bob":20}
print(type(dic))
print(dic["Mike"])
dic["Amy"]=22
print(dic)
print(dic.keys())

#set
s=set([1,2,3]) 
print(type(s))
s.add(1)
s1=set([2,3,4]) 
print(s & s1) 
print(s | s1) 
if 1 in s:
    print "s contain 1"

s = set("hello")
print s