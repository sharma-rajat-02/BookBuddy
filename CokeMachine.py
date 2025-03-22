#Coke Machine
c=50
print("Amount Due:",c)
denominations=[5,10,25]

while True:
    i=int(input("Insert Coin: "))
    if i in denominations:
        c=c-i
        if c<=0:
            c=-c
            print("Change Owned:",c)
            exit()
        else:
            print("Amount Due:",c)
    else:
        print("Amount Due: 50")
        break