#Banking system

class bank:
    def __init__(self,name,acc_no):
        self.bal=0
        self.acc_no=acc_no
        self.name=name
    def deposit(self):
        damount=int(input("\nEnter Amount to be deposited: "))
        if damount>0:
            self.bal+=damount
            print("\nTransaction Successful")
        else:
            print("\nPlease enter valid amount")
        return self.bal
    def withdraw(self):
        wamount=int(input("\nEnter Amount to be withdrawn: "))
        if self.bal>=wamount:
            self.bal-=wamount
            print("\nTransaction Successful")
        else:
            print("\nNot enough balance")
        return self.bal
    def check(self):
        print(f"\nYour account balance is :{self.bal}")
    def display(self):
        print(f"\nAccount Holder's Name: {(self.name).capitalize()}")
        print(f"Account Number: {self.acc_no}")
        print(f"Account Balance: {self.bal}")
objname=input("Enter Account Holder's Name: ")
objacc_no=int(input("Enter Account Number: "))
b=bank(objname,objacc_no)
b.deposit()
b.withdraw()
b.check()
b.display()
# what=input("A. Deposit\nB.Withdraw\nC. Check Balance\nD. Display Details\nWhat do you want to do ? ")
# if what.upper()=="A":
#     bank.deposit()
# elif what.upper()=="B":
#     bank.withdraw()
# elif what.upper()=="C":
#     bank.check()
# elif what.upper()=="D":
#     bank.display()
# else:
#     print("Please enter valid input.")
