#This is lecture 2

#Functions

mylist = [ "5" , "4" , "3" , "2" , "1" , "0" ]
#
mylist.append("-1")                                  #1
print(mylist)
#
mylist.insert(0,"6")                                 #2.1
print(mylist)
#
length=len(mylist)                                         #7
#
mylist.insert(int(length//2),'X')                        #2.2
print(mylist)
#
mylist.insert(-1,"-2")                               #2.3
print(mylist)
#
my_list2=mylist.copy()                                           #3    
print(my_list2)
#
mylist.remove('X')                                 #4
print(mylist)
#
tup=tuple(mylist)                                          #6.1
print(tup)
#
list3=list(tup)                                             #6.2
print(list3)
#
mylist.reverse()
print(mylist)
leng=len(mylist)
print(leng)