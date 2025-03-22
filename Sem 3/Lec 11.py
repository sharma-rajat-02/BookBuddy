#Scope of the variable in python

#Local variables
#Global variables

# x=int(input("What do you want x to be? "))                          #global variable
# def funct(a,b):
#     c=a+b                                                           #local variable
#     print(f"c is a local variable with value = {c}")
# class main:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def main(self):
#         funct(self.num1,self.num2)
#         print(f"x is a global variable with value = {x}")

# n1=int(input("Enter 1st number: "))
# n2=int(input("Enter 2nd number: "))
# main(n1,n2)
# n1.main()
# n2.main()

# school name regno global, marks local print everything with marks.
try:
    f=open("My Details.txt","x")
    f.close()
except FileExistsError:
    pass
def myfile():
    def details(name,regno,school):
        f=open("My Details.txt","a")
        f.write(f"Name: {name}\nRegNo.: {regno}\nSchool: {school}\n")
        f=open("My Details.txt","r")
        f.readlines(3)
        m1(a)
        m2(b)
        m3(c)
        m4(d)
        m5(e)
        f=open("My Details.txt","r")
        print(f.read())
    def m1(m1a):
        f=open("My Details.txt","a")
        f.write(f"Marks of 1st Sub: {m1a}\n")
    def m2(m2a):
        f=open("My Details.txt","a")
        f.write(f"Marks of 2nd Sub: {m2a}\n")
    def m3(m3a):
       f=open("My Details.txt","a")
       f.write(f"Marks of 3rd Sub: {m3a}\n")
    def m4(m4a):
        f=open("My Details.txt","a")
        f.write(f"Marks of 4th Sub: {m4a}\n")
    def m5(m5a):
        f=open("My Details.txt","a")
        f.write(f"Marks of 5th Sub: {m5a}\n")
    n=input("Name: ")
    r=input("Registration No.: ")
    s=input("School: ")
    a=int(input("Marks 1: "))
    b=int(input("Marks 2: "))
    c=int(input("Marks 3: "))
    d=int(input("Marks 4: "))
    e=int(input("Marks 5: "))
    details(n,r,s)
x="Yes"
while True:
    if x=='Yes':
        myfile()
        print("Your file has been updated")
        y=input("Do you want to add a student? {Yes,No} : ")
        y=y.capitalize()
        x=x.replace("Yes",y)
    elif x=='No':
        break
#File Handling

# f=open(r"C:\Users\Dell\Python\Sem 3\Say hello.txt","a")
# f.write("Name:")
