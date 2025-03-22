#Oops in Python

# class Person:
#     def __init__(self,name,age):
#         self.age=age
#         self.name=name
#     def __str__(self):                                #String representation of object entries
#         return f"Name: {self.name} Age:{self.age}"
#     def greet(self):
#         print("Hello,",self.name)
#         tell=input("Do you want me to tell your age? ")
#         if tell.capitalize()=="Yes":
#             print("Your age is:",self.age)
#         else:
#             exit()
# n_ame=input("Enter your name: ")
# a_ge=int(input("Enter your age: "))
# n_ame=n_ame.capitalize()

# p1=Person(n_ame,a_ge)
# print(p1.name)
# print(p1.age)
# print(p1)
# p1.greet()

class student:
    def __init__(self,name,regno,avg):
        self.name=name
        self.regno=regno
        self.avg=avg
    def __str__(self):
        # print(f"Name: {self.name}\nReg. No.: {self.regno}")
        return f"Name: {self.name}\nReg. No.: {self.regno}"
    def avgfunct(self):
        print(self.avg)
M1=int(input('Enter marks M1: '))
M2=int(input('Enter marks M2: '))
M3=int(input('Enter marks M3: '))
M4=int(input('Enter marks M4: '))
M5=int(input('Enter marks M5: '))
tot=M1+M2+M3+M4+M5
average=float(tot/5)
p2=student("Rajat","23BAI10159",average)
print(p2)
p2.avgfunct()



# class bank:
#     def __init__(self,name,accno,bal,city):
#         self.name=name
#         self.accno=accno
#         self.bal=bal
#         self.city=city
#     def __str__(self):
#         return f"Name: {self.name}\nAcc.No: {self.accno}\nBalance: {self.bal}\nCity: {self.city}"
# obj1=bank("John",91672,50000,"Indore")
# print(obj1)