import tkinter
print(dir(tkinter))
# #Calculator program in python
# def calc():
#     a=float(input("Enter 1st number: "))
#     b=float(input("Enter 2nd number: "))
#     # if b==0:
#     #      print("1st number cannot perform any kind of division with 0")
#     #      print("Please enter another number")
#     #      exit()
#     c=a+b
#     d=a-b
#     e=a*b
#     try:
#         f=a/b
#     except ZeroDivisionError:
#         pass
#     else:
#         what=int(input("What do you want to calculate? \n Type \n '1' for addition,\n '2' for subtraction,\n '3' for multiplication,\n '4' for division: "))
#         if what==1:
#             print(c)
#         elif what==2:
#             print(d)
#         elif what==3:
#             print(e)
#         elif what==4:
#                 print(f)
#         else:
#             print("Please choose and operation from above")
# x='Yes'
# while True:
#     if x=='Yes':
#         calc()
#         y=input("Do you want to use the calculator? {Yes,No} : ")
#         y=y.capitalize()
#         x=x.replace("Yes",y)
#     elif x=='No':
#         print("Thankyou for using the calculator!")
#         break