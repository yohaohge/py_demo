people=["Tom", "Tim","Mike"]
print(type(people))
print(people)
print(people[0])

# different type can be together 
something=[123,"string", 3.14] 
print(type(something))
print(something)
print(something[0],something[1])

# change
people[0] = "Lisa"
print(people)

# append 
people.append("Amy")
print(people)
print(len(people))

# pop
something.pop()
print(something)


# insert & delete
something.insert(1,"insert obj")
print(something)
something.pop(1)
print(something)

# tuple can not be changed
staff=("mike","Bob","Tracy")
print(staff)
print(len(staff))

staff[0] = "Lisa" # wrong