#List Operations contd... + Tuples

# tup=('this','is','my','list')
# y=list(tup)
# print(y)
# y.remove('list')
# tup=tuple(y)
# tup1=('tuple',)
# tup+=tup1
# print(tup)



#Packing and Unpacking tuples

# fruits=('Apple','Banana','Grapes')
# (red,yellow,green)=fruits
# print(f'{red} :Red')
# print(yellow,':Yellow')
# print(green,':Green')


#print elements one under the other

# fruits=('Apple','Banana','Grapes')
# i=0
# while i<len(fruits):
#     print(fruits[i])
#     i+=1

# fruits=('Apple','Banana','Grapes')
# for x in fruits:
#     print(x)

# fruits=('Apple','Banana','Grapes','Apple')
# print(fruits.count("Apple"))


#Perform function on an empty list with integers

arr=[]
arr.append(1)
print(arr)
arr.append(2)
print(arr)
arr.insert(1,3)
print(arr)
arr.remove(3)
print(arr)
arr.pop()
print(arr)
a=[2,5,4,3,6]
arr.extend(a)
print(arr)
arr.sort()
print(arr)
arr.reverse()
print(arr)