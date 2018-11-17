# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = 10.5
print(type(a))
print(a)

b=False
print(b)

list1=[10,'@',10.5,'testabcd']
print(list1)
print(type(list1))

print(list1[0])
print(list1[0:4])
list1.append('asdasd')
list1[2]=2000

list1.extend((10,20))
list2=[30]
list1.extend(list2)
print(list1)

print(list1[1])
print(list1[1:3])
print(list1[3:3])

# =============================================================================
# 
# //tuple reffers to [] and list mean () dictinary mean {} key value pair
# tuple mean read only 
#where as list can be edittable
#list and tuple are heterogenoud data types
# =============================================================================
tuple1 = (1,2,3,4)
print(type(tuple1))

tuple2 = (1,2,'test')
print(type(tuple2))

len(tuple2)


#access elements by key 
test = {'length':10,'breadth':20}
print(type(test))
print(test['breadth'])

#alternate way to access elements by key
print(test.get('length'))

#acess both key value pair
print(test.items())

#access keys
print(test.keys())







